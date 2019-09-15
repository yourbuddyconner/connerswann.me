Title: Arduino - An Internet of Things
Date: 2014-06-24 20:51
Author: Conner Swann
Slug: arduino-an-internet-of-things
Category: Arduino
Tags: Arduino, IOT, REST, API, Javascript

Recently I got an Arduino Uno, a small, versatile microcontroller that has been adopted by the "Maker" community as the controller of choice for hobby electronics, and for good reason.

In my limited experience so far, Arduino is a real joy to deal with, having a very simplistic interface while preserving a very robbust "skillset" if you will. The first thing I did was spend a day playing with a box of components, learning how to read sensors and analog components with the board and reacting to those readings, whether it be just reporting back to the computer via serial or prehaps turning on/off an LED.

I've heard the term "Internet of Things" thrown around a lot, but never really quite understood what all the hype was about. However, after screwing around with an internet-equipped Arduino for a day, I can finally appreciate the power of being able to take your physical sensors and hardware and grant them a voice on the great forum that is "The Internet".

To demonstrate this idea, I wired up a photoresistor to my Arduino to take readings of the ambient light, and had it report the values to a Meteor.js server every ten seconds. The code is below, if you get lost or confused, leave a comment, but it's pretty heavily commented and (hopefully) easy to follow.

![Photo Of Project]({attach}/images/2014/arduino-1.jpg)

Disclaimer: This is super-hacked together, I'm not claiming to be a guru. With that said, it works, so I have that going for me.

<pre class="line-numbers">
<code class="language-c">
#include < SPI.h >
#include < Ethernet.h >

// For ethernet shield
byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };// MAC Address  
char server[] = "arduinotest.meteor.com";            // Server to connect to  
// IP Address in case we don't get one from DCHP
IPAddress ip(192,168,0,177);    

EthernetClient client;

// Last time we connected to the server, in milliseconds
unsigned long lastConnectionTime = 0;  
// State of the connection last time through the main loop                
boolean lastConnected = false;  
// Delay between updates, in milliseconds
const unsigned long postingInterval = 5000;        

void setup() {  
    // Open the serial connection
    Serial.begin(9600);
    Serial.println("Initializing Ethernet Shield...");

    if (Ethernet.begin(mac) == 0){
        // DCHP config has failed
        Serial.println("Failed to configure Ethernet using DHCP");
        // Set it up manually
        Ethernet.begin(mac, ip);  
    }
    // Give it a second
    delay(1000);
    Serial.print("IP: ");
    Serial.println(Ethernet.localIP());
}

void loop() {  
    // In case we ever get a response, log it to serial
    // commented out because unnecessary
    // if (client.available()) {
    //  char c = client.read();
    //  Serial.println("RESPONSE INCOMING CAPTAIN!");
    //  Serial.println("==========================");
    //  Serial.print(c);
    //  Serial.println("==========================");
    // }

    // If it's not connected but we've connected recently
    if (!client.connected() && lastConnected) {
        //Serial.println();
        Serial.println("trouble in paradise... disconnecting.");
        client.stop();
    }
    // if you're not connected, and ten seconds have passed since
    // your last connection, then connect again and send data:
    if(!client.connected() && (millis() - lastConnectionTime > postingInterval)) {
        httpRequest();
    }
    // store the state of the connection for next time through
    // the loop:
    lastConnected = client.connected();
}

int httpRequest() {  
    // if there's a successful connection:
    // String postData = String("v=" + analogRead(0));
    if (client.connect(server, 80)) {
        Serial.println("connecting...");
        // send the HTTP POST request:
        client.println(constructRequest());
        client.println("Host: arduinotest.meteor.com");
        client.println("User-Agent: jetpack-rinocerous");
        client.println("Connection: close");
        client.println();


        // let us know it sent
        Serial.println("Sent!");
        // note the time that the connection was made:
        lastConnectionTime = millis();
    } 
    else {
        // if you couldn't make a connection:
        Serial.println("connection failed");
        Serial.println("disconnecting.");
        client.stop();
    }
    return 1;
}

String constructRequest(){  
    String post = "POST ";
    String location = "/yolo?v=";
    int val = analogRead(0);
    String type = " HTTP/1.1";

    return post + location + val + type;
}
</code>
</pre>
In english, the Arduino initializes the Ethernet shield and requests an IP address via DCHP. Assuming that's successful, it enters the loop and periodically tries to connect to my server at arduinotest.meteor.com.

Once connected, about every ten seconds (depending on if the last connection attempt was sucessful or not) it reads the photoresistor and sends a request to the server with the value as a url parameter. It then loops again. The algorithm's also got contingencies for what happens if it can't connect, if you're interested take a look at the code.

That's it for the Arduino code. Once I've added to the Meteor.js server-side code a little bit, I'll make a post about how I accomplished that.