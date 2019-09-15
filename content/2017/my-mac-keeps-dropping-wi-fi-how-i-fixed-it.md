Title: My Mac Keeps Dropping Wi-Fi - How I Fixed It
Date: 2017-11-14
Author: Conner Swann
Slug: my-mac-keeps-dropping-wi-fi-how-i-fixed-it
Category: MacOS
Tags: Wi-Fi, cron, MacOS

I run a lot of things on my Desktop Mac Pro at home -- from basic stuff like a Plex media server to more custom projects like web servers or a VPN gateway. It's pretty important that these semi-critical services stay online as much as possible, however in furtherance of this goal I ran into one major issue: the shape of my house. 

My computer is upstairs and the cable modem is ~200 feet away, through multiple floors, in the basement. I obviously have in-home Wi-Fi, but occasionally the Mac would disconnect from the network with no warning, and the only way to get it back on was to physically be there at the keyboard. Not Optimal! 

It's not a gigantic issue because simply sitting down, logging in, and cycling the Wi-Fi power is all that's needed to reconnect. However, this is really inconvenient if I'm not physically there but still want to consume the media on the machine -- so I set out to fix the problem for good. 

Luckily for me, Apple is really good about providing command-line control over hardware functionality in most circumstances, and Wi-Fi is no exception. There is a handy program on all OS X Machines called `networksetup`. Here's an excerpt from the man page entry: 

```
NAME
     networksetup -- configuration tool for network settings in System Preferences.

DESCRIPTION
     The networksetup command is used to configure network settings typically configured in the System Preferences application.  The networksetup command
     requires at least "admin" privileges to run. Most of the set commands require "root" privileges to run.

     Any flag that takes a password will accept "-" in place of the password to indicate it should read the password from stdin.
```

Knowing that `networksetup` exists and how it works, I set out to whip up a little BASH script that can be run with cron and can check for internet connectivity and cycle the Wi-Fi if necessary. Below is what I came up with: 

<script src="https://gist.github.com/yourbuddyconner/22c37e5246b041fd5c6e4d1e89db0d34.js"></script>


After the script was written, it was trivial to add it to my crontab to be executed once every couple minutes. I also set up external monitoring Namecheap's Dynamic DNS service and UptimeRobot.com, but that's a topic for a future post. 