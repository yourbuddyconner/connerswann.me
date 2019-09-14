Title: Keeping Your University Public
Date: 2015-04-20 22:09
Author: Conner Swann
Slug: keeping-your-university-public

Over the past year or so, I've slowly become aware of the sheer amount of *stuff* my school (Northern Arizona University) buys and how sometimes, I don't agree that a particular thing needed to be bought. Regardless of what's being purchased, from more residence halls and parking (I wish) to contractors, it turns out that pretty much everything is published and freely available due to NAU being a public institution. 

A couple of days ago, one of my friends showed me [a Request for Proposals](http://nau.edu/Contracting-Purchasing-Services/_Forms/Bids/P15JO001/) that NAU had published, detailing a intent to hire "Federal Lobbying Services and Public Relations Consulting." Now, that got me asking some questions. Why exactly does NAU need federal lobbyists and why is this the first time I was hearing about this? 

![]({static}/images/2015/keeping-university-public-lobbying-proposal.png)

As a student, I definitely feel like I am far removed from decisions that often affect me and the general campus community directly. Questions like who is building the new science lab building or how much parking is needed seem to be answered without even consulting the people (students) that the university is (hypothetically) serving. While it is obvious that these proposals are being posted publically, they're posted in areas of the nau.edu website that might be "off the beaten path" for your average student. 

Now, I can agree that most of these decisions are boring and it makes sense to compartmentalize the decision-making process as much as possible. Furthermore, a lot of these issues are horrendously complex, so sometimes they're understandably difficult to summarize. However, I believe an attempt needs to be made to engage the student body, if only passively so that they know projects are taking place.

It was with that sentiment that I decided to throw together a quick proof-of-concept project called [@KeepNAUPublic](http://twitter.com/KeepNAUPublic), a Twitter bot that watches the [NAU Bid Board](http://nau.edu/Contracting-Purchasing-Services/NAU-Bid-Board/) and tweets the title, due date, and a link to the proposal whenever a new RFP is posted. 

<blockquote class="twitter-tweet tw-align-center" lang="en"><p>P15JO001&#10;Req: Federal Lobbying Services and Public Relations Consulting&#10;Link: <a href="http://t.co/E9hoxfuxMO">http://t.co/E9hoxfuxMO</a>&#10;Due: April 21, 2015, at 2:00 PM</p>&mdash; Keep NAU Public (@KeepNAUPublic) <a href="https://twitter.com/KeepNAUPublic/status/590240493943959552">April 20, 2015</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

Currently, the process is pretty basic, however as time goes on I forsee the ability to search proposals for keywords, red-flags, and other things that a student might care about. I forsee this being a nice visualization of when, where and how NAU makes purchasing decisions. 

The bot is implemented with a couple Python libraries including [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/) for HTML scraping and parsing, and [Tweepy](http://www.tweepy.org/) which I used as a Twitter API Client. I've decided to hold off on posting the source code for now until the bot has been significantly more fleshed out, but if you have any questions about how I went about it, feel free to shoot me a tweet [@YourBuddyConner](http://twitter.com/yourbuddyconner)!