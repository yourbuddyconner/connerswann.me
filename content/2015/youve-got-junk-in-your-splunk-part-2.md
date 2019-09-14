Title: You've Got Junk In Your Splunk (Part 2) - An Examination of Real-World Use-Cases for Splunk
Date: 2015-11-30
Author: Conner Swann
Slug: youve-got-junk-in-your-splunk-part-2

<small>This is Part 2 of a multi-part post about the amazing software that is Splunk, if you haven't already, head over to [Part 1](http://connerswann.me/youve-got-junk-in-your-splunk-an-introduction-to-splunk-and-it-data-analysis/) and check it out.</small>

##Case Studies

There is a virtually limitless set of problems that Splunk easily solves. From the usual IT systems analysis to advanced visualization of business trends and statistics, you'd be hard-pressed to find a decently-sized analytics task that Splunk would preform poorly with. 

To illustrate the vast array of *things* Splunk can do, in this and subsequent posts, I'm going to examine two different use-cases for Splunk. This one looks at it from a Business-Analytics perspective and the next one will be from a more traditional IT Intrusion Prevention perspective. 

#7/11 - Indonesia

![7/11 Logo]({static}/images/2015/7-Eleven-Logo.PNG)

##Pre-Splunk
In 2009 7/11, the US gas station and convenience store chain, decided to expand to Indonesia, a new and foreign market to them. This obviously required them to come up with new promotions, sell new products, and predict when customers were going to want a particular product so they were sure to have it in stock.

To be successful in the new region, the company had to compete with pre-existing ["warungs"](https://en.wikipedia.org/wiki/Warung) -- small casual cafes and shops that are ubiquitous across the island nation. To do this, 7/11 stores in the country sold local foods along with the usual soft drinks and convenience store items. In addition, stores also provide amenities like outdoor seating, WiFi, and music to customers to make them more hospitable to a younger middle-class clientele. This allowed them to not only establish a foothold in the country, but thrive and expand to 100+ stores nationwide.

In order to maintain a healthy revenue stream and stay on top of their competition, 7/11 set up information-gathering infrastructure in order to identify trends in their Point of Sale data. However, this system was designed and built on top of their legacy IT systems and was markedly rigid in its processes. As a result, while they were able to glean insights from their data, the process required actual people to manually analyze data for significant portions of the process. From the moment they decided to process data in a time range, it could take as long as 3 months to organize and execute a marketing campaign. While the data *was* available to them and provided useful insights on what their customers wanted at a particular time, the process was far from real-time analysis and ultimately could be improved. 

##Post-Splunk
In 2014, the company began searching for another data analysis platform to give them an edge in Indonesia, and after vetting several other competitors in the space, ended up choosing Splunk. By forwarding logs from Point of Sale systems in each location to a central Splunk cluster and taking advantage of the real-time nature of Splunk's data analytics, 7/11 was able to drastically increase the efficiency of its marketing and promotions machine. 

By adopting Splunk, the company cut their time-to-promotions by over 80%. Whereas before it took over three months to plan and prepare a marketing campaign, after Splunk it only takes them two week's time from the moment they decide to put together a campaign to the point where the campaign is live. In addition, Splunk allows 7/11 to take other data sources into account when deciding what products to stock at any particular time. By consuming weather forecasts from the [Yahoo! Weather API](https://developer.yahoo.com/weather/), they are able to predict when certain products will be in high demand days or weeks in advance. 

As I hope you can see, Splunk is immensely useful when collecting data from IT resources to affect business decisions. The next post in this series will examine how I personally used Splunk at work for a proof-of-concept in Information Security. I leveraged Splunk by collecting data from a series of Raspberry Pi SSH HoneyPots and creating Splunk Alerts when potentially malicious activity appears elsewhere in our system. Stay Tuned!

Source: 
[Splunk Success Story - 7/11](http://www.splunk.com/view/7-eleven-indonesia/SP-CAAAN92)

Do you use Splunk? Have some good ideas about creating value through aggregate data? Hit me up on Twitter and let's talk! [@YourBuddyConner](http://twitter.com/yourbuddyconner)