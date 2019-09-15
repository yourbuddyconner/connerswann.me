Title: An Internet of Things (Part 2): Calling Meteor.js Functions Externally
Date: 2014-06-24 20:54
Author: Conner Swann
Slug: an-internet-of-things-part-2-calling-meteorjs-functions-externally
Category: Arduino
Tags: Arduino, IOT, REST, API, MeteorJS, Javascript

In a previous post I talked about my simple Arduino sketch that contacts a Meteor.js server and feeds it a value read from a Photoresistor. Now I'm going to detail how I hacked together the server. Just an advanced warning, I'm not an expert with Meteor and I'm going to be refining this implementation as I go. With that said, it works, so I've got that going for me.

First, it's probably pertinent to go into a little detail as to what "Meteor.js" is. According to them:

>Meteor is an open-source platform for building top-quality web apps in a fraction of the time, whether you're an expert developer or just getting started.

In a nutshell, it's a javascript framework for writing web apps. One attribute that makes sets it apart is the ability to write both the client-side and server-side applications entirely in Javascript using the handy Meteor library. I think it adds an element of fun/coding/computer-science-ness to (what I consider to be) the drudgery of classic HTML and CSS.

I created a simple Meteor application to interface with my Arduino. The page is tracking a database table called "reads" and whenever another item is added it updates itself with the value from that item's "value" entry in the database. All of this logic happens on the client-side and is contained the following code.

<pre class="line-numbers">
<code class="language-javascript">
Reads = new Meteor.Collection("reads");

if (Meteor.isClient) {  
    // Fills in Templates
    Template.temperature.val = function () {
        val = Reads.find({}, {sort:{timestamp: -1}}, {limit: 1}).fetch()[0];
        if(val){
            Session.set("currentValue", val.value);
        }
        return val;
    };
    Template.temperature.message = function(){
        if(Session.get("currentValue") < 200){
            return "Hey, who turned out the lights?";
        }
      else{
            return "It's totally bright enough to see..."
        }
    };
}
</code>
</pre>
So far, this is all simple out-of-the-box meteor behavior, but since I wanted to play around with calling Meteor functions externally, I added Iron Router to my Meteor app. Iron Router is a "client and server-side router built for use with Meteor." It allows you to route traffic to URLs on your server (or client) to arbitrary templates or even trigger meteor functions.

The code is super uninvolved, simply create a new Iron Router route on the server have it store the URL parameters that have been passed in a database. Meteor handles the ordeal of shuttling that data down to the client, something I find to be very powerful.

<pre class="line-numbers">
<code class="language-javascript">
if (Meteor.isServer) {  
    Router.map(function () {
        this.route('yolo', {
            where: 'server',
            action: function () {
            time = new Date().getTime();
            Reads.insert({value: this.request.query.v, timestamp: time})
        }
    });
    });
}
</code>
</pre>
I created a route at `http://arduinotest.meteor.com/yolo`. You can see that it works for yourself, just copy this: `http://arduinotest.meteor.com/yolo?v=9001` into your url bar and then visit `http://arduinotest.meteor.com`. Assuming the previous value wasn't already "9001", the page should have updated to reflect the changes.

The page actually reacts to the values that are passed, but you'll have to play with it to figure out exactly what makes the text change!