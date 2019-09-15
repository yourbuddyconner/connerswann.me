Title: Arduino: Introducing The Adafruit CC3000 WiFi Shield
Date: 2014-12-29 00:45
Author: Conner Swann
Slug: arduino-introducing-the-adafruit-cc3000-wifi-shield
Category: Arduino
Tags: Arduino, IOT, HTTP, Ethernet Shield

I recently got my hands on an [Adafruit CC3000 WiFi Shield](http://www.adafruit.com/product/1491). From the Adafruit product page: 
>"The CC3000 hits that sweet spot of usability, price and capability. It uses SPI for communication (not UART!) so you can push data as fast as you want or as slow as you want. It has a proper interrupt system with IRQ pin so you can have asynchronous connections. It supports 802.11b/g, open/WEP/WPA/WPA2 security, TKIP & AES. A built in TCP/IP stack with a "BSD socket" interface. TCP and UDP in both client and server mode, up to 4 concurrent sockets."

In not so many words, it's a piece of hardware that can be used to connect your Arduino to a WiFi access point to send and recieve data wirelessly. It's a pretty robust piece of hardware, and it's perfect to connect my "Internet of Things" projects to the internet. 

To get my setup working, I stepped through the [Adafruit Documentation on the CC3000](https://learn.adafruit.com/adafruit-cc3000-wifi) which is complete and very thorough. 

Before you can start using this board, you have to solder on the headers so you can plug it directly into the Arduino. 

*Since I'm more of a software guy, I won't detail the actual process of soldering the headers, but if you're looking for instructions [Adafruit has you covered](https://learn.adafruit.com/adafruit-cc3000-wifi/assembly-and-wiring).*

![Arduino with WiFi Shield]({attach}/images/2014/arduino-wifi-shield-1.jpg)

To get it running, you have to add the shield's code libraries to your ```arduino_sketch_location/libraries/``` folder, the library is available for download along with installation instructions [here](https://learn.adafruit.com/adafruit-cc3000-wifi/cc3000-library-software).

From there, all I did was pop the shield into place on top of the Arduino and load up the 'buildtest' example file [1]. 

I got an output that looked like this: 
<pre>
<code class="language-none">
Hello, CC3000!

RX Buffer : 131 bytes
TX Buffer : 131 bytes
Free RAM: 1221

Initialising the CC3000 ...
Firmware V. : 1.24
MAC Address : 0x08 0x00 0x28 0x57 0xA4 0xF5
Networks found: 10
================================================
SSID Name    : AtlantisBack
RSSI         : 63
Security Mode: 1

SSID Name    : DIRECT-c0[BD]EM59
RSSI         : 55
Security Mode: 3

SSID Name    : Someone's Wi-Fi Network
RSSI         : 37
Security Mode: 3

SSID Name    : Atlantis
RSSI         : 55
Security Mode: 1

================================================

Deleting old connection profiles

Attempting to connect to Atlantis
Connected!
Request DHCP

IP Addr: 192.168.1.134
Netmask: 255.255.255.0
Gateway: 192.168.1.1
DHCPsrv: 192.168.1.1
DNSserv: 76.14.0.8
www.adafruit.com -> 207.58.139.247

Pinging 207.58.139.247...5 replies
Ping successful!


Closing the connection
</code>
</pre>

This is just a really basic example so I could prove to myself that I could get the shield working. However, my end-goal is to get the board speaking to a server and reporting some values, similarly to what I did in a [previous post with an Ethernet shield](http://connerswann.me/arduino-an-internet-of-things/). 

Stay tuned!
[^1]: The documentation actually says that you shouldn't be able to run the Arduino and the CC3000 shield off of your computer's USB port due to power consumption being too high, however I wasn't able to verify this. It might be a problem as you get into more advanced things and require more of the Arduino's pins to be powered. 