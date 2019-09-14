Title: Hack AZ: Postgame Report
Date: 2015-03-11 06:54
Author: Conner Swann
Slug: hack-az-postgame-report

![](/../../images/2015/hack-az-cover.jpg)

This past weekend, I went to [Hack Arizona](hackarizona.org), Arizona's first-ever college Hackathon hosted at the University of Arizona in Tucson. 

#### hack·a·thon

ˈhakəˌTHän/
noun informal
*an event, typically lasting several days, in which a large number of people meet to engage in collaborative computer programming.
"a series of 48-hour hackathons to build new web and mobile services"*

Of all the trends the past couple of years have brought, I have to say that Hackathons are probably the coolest. Together in small groups (~1-6), college and high school-aged students get together and over the course of a sleep-deprived weekend, they create cool hardware or software projects! 

![]({static}/images/2015/hack-az-1.jpg)

I had found out a couple days before the event that Raytheon Missile Systems was sponsoring a drone challenge, and when I told my team the "Hack Jacks" (consisting of my friends Brandon Paree and Dylan Grayson, along with myself) about it, they were more than interested. 

Raytheon had purchased 15 [Parrot AR.Drone 2.0](http://ardrone2.parrot.com/)'s, for the purpose of renting them out to teams at Hack AZ so they could write code and hack on them. Each member of the teams with the best hacks would then walk away with their own AR Drone! As luck would have it, we ended up getting to the UA campus early enough to snag one.

The AR.Drone platform is an amazing beast, it's a quadcopter with a linux box its core. It also has a slick C software development kit, making it relatively easy to get these things to basically fly themselves. It turns out that a nice guy named [felixge](https://github.com/felixge/) made a cool NodeJS library called [Node AR-Drone](https://github.com/felixge/node-ar-drone) which ports many of those C bindings into the [only real dev language](https://www.youtube.com/watch?v=ame2PH67gnk). 

![]({attach]/images/2015/hack-az-drone-app.gif)
 
We decided that we wanted to make our drone autonomous, so we leveraged the [OpenCV](http://opencv.org/) Computer Vision library to do face tracking. 

In a nutshell, we built a basic AI that reads frames from the AR Drone's HD camera and searches them for faces. If no suitable objects are immediately visible, the drone enters a search pattern, slowly panning its view until it can see a face. Once it finds a trackable object, the drone changes course and follows it, adjusting its orientation and altitude to keep the face both centered and a constant size in its view (and thus, a constant distance away). It's key to note here that this incorporates basic guidance control elements as well as object identification and collision avoidance. 

This project was particularly challenging for the three of us, because none of us had any major graphics experience before. We ended up spending the majority of the time reading OpenCV source code and documentation. Unfortunately, with big projects like that it's easy to get lost in their complexity! However, despite the gaps in our knowledge, we picked a project that we felt we could demo well, and that we did. This is a major part of the hackathon, without a good demo, your project is nothing!

When it came time to show off our hack, many of the other teams had trouble getting their drones off the ground, whether it be from quirky code written out of sleep deprevation or other hardware issues. Our presentation in contrast, went off incredibly smoothly. 

We showcased the facial recognition and search capabilities by first having my teammate Brandon stand in front of the drone to allow it to acquire a lock on his face. He then covered his face with a hand, waited as the drone panned over to the crowd, and much to our delight, it actually acquired a lock and drifted over to look at a spectator! I then had the entire group of people around me cover their faces, and agiain, the drone began to search for another target. 

After all the demos were done, the judges walked off the field to deliberate. After almost an hour, they came back with decisions and we ended up placing third out of more than ten teams!

![]({static}/images/2015/hack-az-2.jpg)

This also meant we'd be going home with our very own Parrot AR Drones! 

Over the course of the weekend, I feel like I learned more than I really expected to. I met a bunch of really cool, like-minded people, and being in that sort of environment is both very enriching and a lot of fun. 

- The guys at Raytheon (Jonathan, Don, Dennis and more!) were a huge help to us, they went out to the field to help us test our program every time, giving us hours of their time. At the end of the weekend, the probably came out just as tired as we were!
- The Hack AZ organizers deserve a round of applause, we really appreciated the fact that the event had the entire Schence and Engineering Library at UA to itself for the majority of the weekend. 
- Ellen, thanks for hanging out with us and taking all those cool pictures!

If you'd like to check out our code, [the entire project is on Github](https://github.com/yourbuddyconner/drone-hackaz/tree/master/Hack-AZ). We've also begun to change and refactor our original gross hackathon code, and it's begun to take shape [here](https://github.com/yourbuddyconner/drone-hackaz/tree/master/v1.0). 


Post-Hackathon, the project consists of an in-browser command-and-control center for the Parrot AR Drone, complete with gamepad support and first-person, bottom camera view, basic telemetry and a battery indicator. There are plenty of features on the roadmap, including more autonomous functionality and FPV goggle support. 

![]({static}/images/2015/hack-az-drone-app.gif)

If you're interested in drones, interested in the project, or have any cool tips or tricks when it comes to Javascript image manipulation, feel free to give me a shoutout on Twitter [@YourBuddyConner](http://twitter.com/yourbuddyconner)

