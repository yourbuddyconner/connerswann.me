Title: MyCI - A Look Into My Personal Cloud Environment
Date: 2017-05-04 20:14
Author: Conner Swann
Slug: myci-a-look-into-my-personal-cloud-environment
Category: Infrastructure
Tags: continuous integration, rancher, docker, drone-ci 
Cover: images/2017/Leveraging-the-Cloud-Featured-Image.jpg

# Why Do I Need a Personal Cloud Environment?
For a long time now, I have enjoyed doing personal software projects that teach me new skills, frameworks or even programming languages. I think that an engineer in a computer-science-related field should always be learning new technology and innovating. However, at times it can be a real struggle to get anything done quickly. When it comes to complex web-based systems there's so much that goes into learning a new language or framework that the entire process quickly becomes overwhelming. 

This is a common problem that many small companies and startups face, and it's one I have personally run into time and time again in my personal projects. Due to the layered nature of web-based communications, there's potentially a _lot_ involved when setting up a development environment. That overhead can at times discourage me from even starting a cool new project to begin with, and that's no fun!

My training and experience as a DevOps Engineer however comes in handy in this situation, so I set out to solve this tricky problem for myself. 

## How Does It Help Me? 
I tend to take the computer scientist's approach whenever possible, and this tricky infrastructure problem is no exception. The Computer Science approach is traditionally "work smarter, not harder," so in that vein my motto for infrastructure is the following: 

> "If you're doing something manually, you're doing something wrong."

> -Conner Swann

Any good DevOps automation system acts like a 10x multiplier for efficiency to a talented software engineer. It allows them to automate the tedium of their day-to-day and spend more time on software issues, which not only increases developer happiness but the happiness of their managers.

I designed my personal cloud infrastructure with this in mind. The system reacts to triggers in my software development cycle and kicks off complex jobs and workflows that I would have started manually, almost before I considered doing it myself. 

# What Is My Stack?

## Docker
I love Docker. The current trend of containerization in tech has provided an incredibly powerful tool and abstraction that software developers everywhere can leverage to drastically increase efficiency. I use Docker because it allows the Software Engineer in me ignore the underlying hardware and focus entirely on the interaction between my code and the dependencies inside the container. 

One of my biggest gripes when I started coding was the dreaded conflicting dependency on my development machine. It's entirely possible to have one project that requires Python 2.7 and another that requires Python 3. If you don't necessarily know your way around a package manager, or worse you don't have access to one, you might be in for a bad time. 

Docker saves you from this by compartmentalizing the application and all its dependencies in a special "box" that is logically separated from all the other "boxes" that share the resources of the host machine. In this way, it saves you a lot of the headache when trying to get two applications you wrote to play nicely together on one host.

![]({static}/images/2017/Docker-API-infographic-container-devops-nordic-apis.png)

## Container Orchestration
Once you figure out how powerful Docker can be, you ask the next logical question: 
> "How can I run a bunch of Docker containers at once?" 

This doesn't necessarily have a concrete answer. 

You could use Google's [Kubernetes](https://kubernetes.io/) or [Apache Mesos](http://mesos.apache.org/), however, if most of your Docker experience is with Docker-Compose in a development environment, learning one or the other can be a blocker to even getting your personal cloud setup! Both Kubernetes and Mesos are amazing, enterprise-grade container orchestration systems in their own right, but unless you have experience using them, it's overkill for your average free-time software developer.

<div class="image-div" style="width: 400px;">
![]({static}/images/2017/SWARM.png)
</div>

You can use [Docker Swarm](https://docs.docker.com/engine/swarm/), however container management is entirely through the CLI. If you want a web-based UI to make your life easier, you're out of luck because the UI offering from Docker inc. is enterprise-only and [_very_](https://www.docker.com/pricing) expensive.  While Docker (the company) isn't helping out hackers wrangle their containers, it's worth mentioning that there are open-source alternatives like [Portainer](http://portainer.io/) and [Shipyard](https://shipyard-project.com/) which do provide web UIs for Docker Swarm. 

The solution I eventually decided on is a free and open-source container management and orchestration software named [Rancher](http://rancher.com/). Rancher checks all my boxes: 

- It's Docker-based and natively supports Docker-Compose for stack definition.
- It's free and open-source.
- It's easy to install and configure. 
- It's backed by a wonderful community and core development team that are very responsive to issues and suggestions on Slack and at meetups.
- It has a web-based UI that I can use to visually manage my containers. 

Because Rancher lets me so easily launch and manage containers, I can easily run an arbitrary number of web-based services. It's trivial to add more Docker hosts to your environments, meaning I can start small and scale up when I need more resources.  
![Rancher]({static}/images/2017/Rancher-Logo-Final-300x180.png)

##Continuous Integration and Deployment
Now that the infrastructure is set up and running, it's time to start thinking about how you're going to run your own software on it. I personally am really annoyed by repetitive tasks and strive to streamline my development cycle as much as much as possible. 

I've used [Jenkins](https://jenkins.io/) extensively at work, and while he's a real workhorse he's a bit overkill for my purposes. Instead, I use [Drone](https://github.com/drone/drone) a container-first Continuous Delivery platform built on Docker, and written in Go. It's still a fairly young project, but what's there currently is more than sufficient for my needs. 

Drone integrates with Github and Rancher! All I have to do is add a configuration file called `.drone.yml` to my root directory and place it with git. It makes my life easy by automatically connecting to my Github account and configuring selected repositories for webhook delivery. When I push code to one of my repos, Drone is automatically notified and a build begins automatically. 


A build consists of first, testing the code using application-specific tests in each repository. Then if all that passes, a Docker container with the application is packaged up and uploaded to the Dockerhub image registry. Lastly, once the image has arrived at the registry, Drone makes an API call to Rancher and upgrades an existing service in place with the new image. 

Regardless of success or failure, Drone then sends a Slack message informing me of the outcome and a link to the build UI. 

![Drone CI Screenshot]({static}/images/2017/drone-ci-screenshot.png)

#Putting it Together
To demonstrate the power of this CI system, I made a quick little example project that I've thrown up on Github. It's a little flask app that returns "Hello World!" when you make a GET request to it. 

It's hosted here. But here's some of the juicy code so you don't have to go so far. 

This is the `.drone.yml` file, which is basically where all the magic happens:
<pre class="line-numbers">
<code class="language-python">
pipeline:
  test:
    image: python:2.7
    commands: 
      - pip install -r application/requirements.txt
      - python application/tests.py
  publish:
    image: docker
    commands:
      - docker login -u "$DOCKER_USERNAME" -p "$DOCKER_PASSWORD"
      - docker build -t yourbuddyconner/docker-hello-world .
      - docker push yourbuddyconner/docker-hello-world
    environment:
      - DOCKER_USERNAME=${DOCKER_USERNAME}
      - DOCKER_PASSWORD=${DOCKER_PASSWORD}
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
  deploy: 
    image: peloton/drone-rancher
    url: http://rancher.swannairlines.com
    access_key: ${RANCHER_ACCESS}
    secret_key: ${RANCHER_SECRET}
    service: hello-world/hello-world
    docker_image: yourbuddyconner/docker-hello-world:latest
    confirm: true
    timeout: 120
  slack:
    image: plugins/slack
    webhook: https://hooks.slack.com/services/...
    recipient: conner
    template: >
      {{#success build.status}}
        Build {{build.number}}  for {{repo.name}}/{{build.branch}} succeeded. Good job.
      {{else}}
        Build {{build.number}}  for {{repo.name}}/{{build.branch}} Failed. You suck.
      {{/success}}
      Build Link: {{build.link}}
</code>
</pre>

This setup makes it ridiculously easy for me to launch a large number of containers running homebrew software with minimal interference from me. I can push code, go make coffee, and come back knowing that there's a new build of my code online. Well... either that or I messed up somewhere and I'm going to have a lead on how to fix it when I sit down.

If you have any questions or comments about this blog post, feel free to tweet me [@Yourbuddyconner](http://twitter.com/yourbuddyconner)!