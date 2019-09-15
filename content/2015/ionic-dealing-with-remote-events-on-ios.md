Title: Ionic: Dealing with Remote Events on iOS
Date: 2015-01-23 18:03
Author: Conner Swann
Slug: ionic-dealing-with-remote-events-on-ios
Category: Ionic
Tags: Ionic Framework, Hybrid Apps, Javascript, iOS

For the past couple semesters, I've been working on an [Ionic](http://ionicframework.com/) app for my university's radio station. Ionic is a "hybrid" framework, that is, the main body of the app is written using web technology (AngularJS, HTML, CSS) and that is coupled with Cordova, a piece of softeware that provides an interface between the web view and the bare metal of the phone. 

Among other things, the app needed to be able to play the station's audio stream. Since I've been focusing primarily on the iOS portion of the universal app, a while back I decided it would be really cool if I were able to control the audio from the lockscreen. However, while the documentation for the Objective C side of it is pretty abundant, there's little to none discussing connecting this with Cordova. 

![Lockscreen Controls]({static}/images/2015/ionic-ios-screenshot.png)


Not knowing exactly where to begin, I found and installed this Cordova plugin from Shi11 called [RemoteControls](https://github.com/shi11/RemoteControls). It provides a couple ObjC methods that allow you to update the track meta and respond to any remote events that your app might recieve. 

The thing is, on the Objective C side Apple is very particular about [which views can and cannot recieve remote events](https://developer.apple.com/library/ios/documentation/EventHandling/Conceptual/EventHandlingiPhoneOS/Remote-ControlEvents/Remote-ControlEvents.html). The procedure is simple, but in practice with Cordova it gets tricky:

> - **Be the first responder.** The view or view controller that presents the multimedia content must be the first responder.
- **Turn on the delivery of remote control events.** Your app must explicitly request to begin receiving remote control events.
- **Begin playing audio.** Your app must be the “Now Playing” app. Restated, even if your app is the first responder and you have turned on event delivery, your app does not receive remote control events until it begins playing audio.

The last bullet is where the trouble started for me. To handle the streaming audio, I'm currently using [Cordova Audio Stream](https://github.com/keosuofficial/cordova-audio-stream-plugin). It leverages the [AvPlayer](https://developer.apple.com/library/mac/documentation/AVFoundation/Reference/AVPlayer_Class/index.html) class to play the audio separately from the webview. 

Now, herein lies the problem. If you follow the documentation for RemoteControls, you will subscribe for remote events within your MainViewController.m, the controller for the WebView. However, since the audio is being instantiated and played from a totally different file within the plugins directory (CDVStream.m) the remote events never get sent to the app. I believe this is because the file that requests the remote events must also be the file that instantiates and plays the audio object. 

SO! If you're following, you can probably guess the solution to this problem. Instead of modifying the MainViewController.m I added the remote events subscription to CDVStream.m where the audio was being played from and voila! It works. 

Coming from a primarily web background, this totally wasn't intuitive for me at all, so hopefully this helps someone in the long run! 

Here's my version of my CDVStream.m, the same logic can easily be duplicated in any file that plays audio more than likely: 

<pre class="line-numbers">
<code class="language-objectivec">
/*
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements. See the NOTICE file
distributed with this work for additional information
regarding copyright ownership. The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, either express or implied. See the License for the
specific language governing permissions and limitations
under the License.
*/

#import "CDVStream.h"
#import "RemoteControls.h"

@implementation CDVStream

@synthesize objAVPlayer;

- (void)create:(CDVInvokedUrlCommand*)command
{
	[self.commandDelegate runInBackground:^{
    	CDVPluginResult* result = [CDVPluginResult resultWithStatus:CDVCommandStatus_OK];
    	[self.commandDelegate sendPluginResult:result callbackId:command.callbackId];
    }];

}

- (void)startPlayingAudio:(CDVInvokedUrlCommand*)command
{
		// begin recieving remote events
        [[UIApplication sharedApplication] beginReceivingRemoteControlEvents];
    	NSString* resourcePath = [command.arguments objectAtIndex:1];
    	NSURL* resourceURL = [NSURL URLWithString:resourcePath];
    	NSLog(@"Now Playing '%@'", resourcePath);
    	if([self objAVPlayer] == nil){
    		[self setObjAVPlayer:[[AVPlayer alloc] initWithURL:resourceURL]];
			[[self objAVPlayer] addObserver:self forKeyPath:@"status" options:0 context:nil];
		}else{
		 	[[self objAVPlayer] play];
		}
    	return;
}
- (void)remoteControlReceivedWithEvent:(UIEvent *)receivedEvent
{
	// where to send the events when they are recieved
    [[RemoteControls remoteControls]
     receiveRemoteEvent:receivedEvent];
}

- (void) observeValueForKeyPath:(NSString *)keyPath 
                                ofObject:(id)object 
                                change:(NSDictionary  *)change 
                                context:(void *)context {

    if (object == [self objAVPlayer] && [keyPath isEqualToString:@"status"]) {
        if ([self objAVPlayer].status == AVPlayerStatusReadyToPlay) {
        	//Audio session is set to allow streaming in background
            AVAudioSession *audioSession = [AVAudioSession sharedInstance];
            [audioSession setCategory:AVAudioSessionCategoryPlayback error:nil];
            [[self objAVPlayer] play];
        }
        if ([self objAVPlayer].status == AVPlayerStatusFailed) {
            NSLog(@"Something went wrong: %@", [self objAVPlayer].error);
        }
    }
}


- (void)stopPlayingAudio:(CDVInvokedUrlCommand*)command
{
	[[self objAVPlayer] pause];
    // I don't want to stop recieving events when the user presses "pause" 
    // so I dont ever stop recieving events
    // I'm relying on the fact that music is no longer playing to halt the events
    //[[UIApplication sharedApplication] endReceivingRemoteControlEvents];

}

@end
</code>
</pre>
