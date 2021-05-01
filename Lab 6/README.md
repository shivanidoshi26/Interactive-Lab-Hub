# m[Q](https://en.wikipedia.org/wiki/QAnon)tt[Anon](https://en.wikipedia.org/wiki/QAnon): Where We Go One, We Go All

## Prep

1. Pull the new changes
2. Install [MQTT Explorer](http://mqtt-explorer.com/)
3. Readings 
   * [MQTT](#MQTT)
   * [The Presence Table](https://dl.acm.org/doi/10.1145/1935701.1935800) and [video](https://vimeo.com/15932020)

## Collaborators

I worked with Ritika Poddar on this lab (rp477). I focussed on coding and communicating the dance steps she (as the dancer) had to make. I primarily used the LED buttons and she used the capacitive touch sensor. 

Here is a link to my code: 
https://github.com/shivanidoshi26/Interactive-Lab-Hub/blob/Spring2021/Lab%206/DDR/ddr_buttons.py

Here is a link to her code:
https://github.com/shivanidoshi26/Interactive-Lab-Hub/blob/Spring2021/Lab%206/DDR/ddr_cap.py

We came up with this idea together after lots of brainstorming, so we hope you enjoy! Here is the link to her repo: https://github.com/Rpoddar1953/Interactive-Lab-Hub/tree/Spring2021/Lab%206.

I would also like to mention that I used the beloved song Disco Inferno by The Trammps as the background song to one of our videos (we do not own the rights to this song: https://www.youtube.com/watch?v=A_sY2rjxq6M). I used this song because it was the only one that came to mind when I think back to my DDR days. I hope it was soothing.

## Introduction

The point of this lab is to introduce you to distributed interaction. We've included a some Natural Language Processing (NLP) and Generation (NLG) but those are not really the emphasis. Feel free to dig into the examples and play around the code which you can integrate into your projects. However we want to emphasize the grading will focus on your ability to develop interesting uses for messaging across distributed devices. 

## MQTT

MQTT is a lightweight messaging portal invented in 1999 for low bandwidth networks. It was later adopted as a defacto standard for a variety of Internet of Things (IoT) devices. 

### The Bits

* **Broker** - The central server node that receives all messages and sends them out to the interested clients. Our broker is hosted on the far lab server (Thanks David!) at `farlab.infosci.cornell.edu/8883`
* **Client** - A device that subscribes or publishes information on the network
* **Topic** - The location data gets published to. These are hierarchical with subtopics. If you were making a network of IoT smart bulbs this might look like `home/livingroom/sidelamp/light_status` and `home/livingroom/sidelamp/voltage`. Subscribing to `home/livingroom/sidelamp/#` would give you message updates to both the light_status and the voltage. Because we use this broker for a variety of projects you have access to read, write and create subtopics of `IDD`. This means `IDD/ilan/is/a/goof` is a valid topic you can send data messages to.
*  **Subscribe** - This is a way of telling the client to pay attention to messages the broker sends out on that topic. You can subscribe to a specific topic or subtopics. You can also unsubscribe
* **Publish** - This is a way of sending messages to a topic. You can publish to topics you don't subscribe to. Just remember on our broker you are limited to subtopics of `IDD`

Setting up a broker isn't much work but for the purposes of this class you should all use the broker we've set up for you. 

### Useful Tooling

Debugging and visualizing what's happening on your MQTT broker can be helpful. We like [MQTT Explorer](http://mqtt-explorer.com/). You can connect by putting in the settings from the image below.



![input settings](https://github.com/FAR-Lab/Interactive-Lab-Hub/blob/Spring2021/Lab%206/imgs/mqtt_explorer.png?raw=true)



Once connected you should be able to see all the messaged on the IDD topic. From the interface you can send and plot messages as well.



## Send and Receive 

[sender.py](./sender.py) and and [reader.py](./reader.py) show you the basics of using the mqtt in python.  Lets spend a few minutes running these and seeing how messages are transferred and show up. 

**Running Examples**

* Install the packages from `requirements.txt`, ideally in a python environment. We've been using the circuitpython environment we setup earlier this semester. To install them do `pip install -r requirements.txt`
* to run `sender.py` type `python sender.py` and fill in a topic name, then start sending messages. You should see them on MQTT Explorer
* to run `reader.py` type `python reader.py` and you should see any messages being published to `IDD/` subtopics.

## Streaming a Sensor

We've included an updated example from [lab 4](https://github.com/FAR-Lab/Interactive-Lab-Hub/tree/Spring2021/Lab%204) that streams sensor inputs over MQTT. Feel free to poke around with it!

## The One True ColorNet

It is with great fortitude and resilience that we shall worship at the altar of the *OneColor*. Through unity of the collective RGB we too can find unity in our heart, minds and souls. With the help of machines can  overthrow the bourgeoisie, get on the same wavelength (this was also a color pun) and establish [Fully Automated Luxury Communism](https://en.wikipedia.org/wiki/Fully_Automated_Luxury_Communism).

The first step on the path to *collective* enlightenment, plug the [APDS-9960 Proximity, Light, RGB, and Gesture Sensor](https://www.adafruit.com/product/3595) into the [Pi Display](https://www.adafruit.com/product/4393).

<img src="https://cdn-shop.adafruit.com/970x728/3595-03.jpg" height="300">

You are almost there!

The second step to achieving our great enlightenment is to run `python color.py`

You will find the two squares on the display. Half is showing an approximation of the output from the color sensor. The other half is up to the collective. Press the top button to share your color with the class. Your color is now our color, our color is now your color. We are one. 

I was not super careful with handling the loop so you may need to press more than once if the timing isn't quite right. Also I have't load tested it so things might just immediately break when every pushes the button at once.

You may ask "but what if I missed class?"

Am I not admitted into the collective enlightenment of the *OneColor*?

Of course not! You can got to [https://one-true-colornet.glitch.me/](https://one-true-colornet.glitch.me/) and become one with the ColorNet on the inter-webs.

Glitch is a great tool for prototyping sites, interfaces and web-apps that's worth taking some time to get familiar with if you have a chance. Its not super pertinent for the class but good to know either way. 



## Make it your own

Find at least one class (more are okay) partner, and design a distributed application together. 

**1. Explain your design** 

Most people at some point in their lives has been to the arcade and walked passed the glorious **Dance Dance Revolution** game. It's both really embarrassing and really fun at the same time. But you have no control over what moves you're given - you just follow the rhythm of a song and try to keep up with the arrows on the screen. For our project, we decided to emulate that entire experience, but to actually give a person the ability to control the other person's moves. 

To break it down, we made use of communication between 2 pis to accomplish this. The 2 pis communicated over 2 topics: IDD/move_setter and IDD/dance_moves. The first MQTT system sent messages over IDD/move_setter and read the messages being sent on IDD/dance_moves. The second MQTT system did the exact opposite of this (read messages coming from IDD/move_setter and sent messages on IDD/dance_moves). The first MQTT system controlled what moves were sent to the second system. Subsequently, the second MQTT performed the move and this was sent back to the first system. The move was verified by the first system and the score incremented. If there was any mismatch, the game ended and the score was reset to 0. 

In DDR, you don't only go left, right, up and down - you can also get a move that requires you to jump on both the left and right arrow or both the up and down arrow or some other combination. This complexity makes the game all the more fun and tiring, so don't worry, we got it covered too! 

**2. Diagram the architecture of the system.** Be clear to document where input, output and computation occur, and label all parts and connections. For example, where is the banana, who is the banana player, where does the sound get played, and who is listening to the banana music?

**3. Build a working prototype of the system.** 

This is what the design of the MQTT 1 system looks like (the controller):

<img src="https://github.com/shivanidoshi26/Interactive-Lab-Hub/blob/Spring2021/Lab%206/DDR/setup1.jpg" height="500">

This is what the design of the MQTT 2 system looks like (the dancer):

<img src="https://github.com/shivanidoshi26/Interactive-Lab-Hub/blob/Spring2021/Lab%206/DDR/setup2.jpg" height="500">

The controller is intended to be small and handheld. It's hidden from the dancer, so they don't know what to expect until they receive the actual message. The actual raspberry pi wasn't fastened at the back - though it very easily could've been - so that it could be moved around if any changes were necessary.

The dancer setup is very much like how the actual dance dance revolution setup is. The dancer stands in the center of the different move buttons (left, right, up and down). They use their feet to press on the corresponding move and perform their dance! It was difficult to not have the wires hidden within the setup because we used a blanket to avoid any slippage as a result of stepping on any of the cardboard cutouts. We definitely acknowledge that the raspberry pi, capacitive sensor and speaker were in very precarious locations.

It is quite clear from the setup of our system what this tool actually is - it wouldn't take someone new very long to figure out how to use it (once all the files are running, of course). We believe they would know what to expect pretty easily. Potentially, the only issue they may have is not pressing the buttons long enough (due to some time delays, the button pressing can be finicky sometimes). 

**4. Document the working prototype in use.** 

As mentioned earlier for our setup, we needed to establish a communication between the 2 pis: Ritika's and mine. Below is a video of how MQTT 1 (my pi) communicated instructions to the other. Note that in the video, the terminal on the left demonstrates the output of running DDR/reader.py, which subscribes to only the topics that we communicated on (IDD/move_setter and IDD/dance_moves), and the terminal on the right demonstrates the output of running DDR/ddr_buttons.py, which prints out a statement when a message is received from the other pi.

[![](https://res.cloudinary.com/marcomontalbano/image/upload/v1619829202/video_to_markdown/images/google-drive--1VZZ9q4U6mQw8xqC_Lzx7PN2ZBavJ03xZ-c05b58ac6eb4c4700831b2b3070cd403.jpg)](https://drive.google.com/file/d/1VZZ9q4U6mQw8xqC_Lzx7PN2ZBavJ03xZ/view?usp=sharing "")

Below is a video of how MQTT 2 (Ritika's pi) communicated instructions to the other. Note that both the video above and the one below were happening at the same time (but I chose to not have my voice played as the voice over once again, so I hope you enjoy the groovy music we replaced it with):

[![](https://res.cloudinary.com/marcomontalbano/image/upload/v1619828699/video_to_markdown/images/google-drive--16DYeWFtuxTt8BZH7ZiavFW49ectT8ye6-c05b58ac6eb4c4700831b2b3070cd403.jpg)](https://drive.google.com/file/d/16DYeWFtuxTt8BZH7ZiavFW49ectT8ye6/view?usp=sharing "")

The system worked mostly quite flawlessly. The only major issues we had were some misalignment between messages sent from the first pi and then from the second pi. We also had  issues with messages being sent more than once, which is why we incorporated some time delays. Overall, we're very proud of our creation!

**5. BONUS (Wendy didn't approve this so you should probably ignore it) get the whole class to run your code and make your distributed system BIGGER.**

Maybe in future iterations of our DDR, we can incorporate a multiplayer mode which could involve more people. However, they would need the phenomenal setup that we built for our system to do so. In general, I believe that games that require lots of equipment won't work well when expanded to multiple users.

It would also be fun to have stages or levels of difficulty incorporated. However, given the time constraint and the speed at which the communication was conducted it might be difficult to get to expert levels. It also may be a bit of hazard to have someone violently jumping around on a blanket, which could very easily slip resulting in some damage in both technical equipment and personal equipment (if you catch my drift).
