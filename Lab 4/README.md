# Ph-UI!!!

For lab this week, we focus on the prototyping the physical look and feel of the device. _Make sure you read all the instructions and understand the whole of the laboratory activity before starting!_



## Prep

1. Pull the new Github Repo.
2. Readings: 

* [What do prototypes prototype?](https://www.semanticscholar.org/paper/What-do-Prototypes-Prototype-Houde-Hill/30bc6125fab9d9b2d5854223aeea7900a218f149)

* [Paper prototyping](https://www.uxpin.com/studio/blog/paper-prototyping-the-practical-beginners-guide/) is used by UX designers to quickly develop interface ideas and run them by people before any programming occurs. 

* [Cardboard prototypes](https://www.youtube.com/watch?v=k_9Q-KDSb9o) help interactive product designers to work through additional issues, like how big something should be, how it could be carried, where it would sit. 

* [Tips to Cut, Fold, Mold and Papier-Mache Cardboard](https://makezine.com/2016/04/21/working-with-cardboard-tips-cut-fold-mold-papier-mache/) from Make Magazine.

* [Surprisingly complicated forms](https://www.pinterest.com/pin/50032245843343100/) can be built with paper, cardstock or cardboard.  The most advanced and challenging prototypes to prototype with paper are [cardboard mechanisms](https://www.pinterest.com/helgangchin/paper-mechanisms/) which move and change. 

<img src="https://dysonthedesigner.weebly.com/uploads/2/6/3/9/26392736/427342_orig.jpg"  width="200" > Dyson Vacuum cardboard prototypes


### For lab, you will need:

1. Cardboard (start collecting those shipping boxes!)
1. Cutting board
1. Cutting tools
1. Markers
1. Found objects and materials--like bananas--we're not saying that to be funny.


### Deliverables for this lab are: 
1. Sketches/photos of device designs
1. "Looks like" prototypes: show us what how the device should look, feel, sit, weigh, etc.
3. "Works like" prototypes: show us what the device can do
4. "Acts like" prototypes: videos/storyboards/other means of showing how a person would interact with the device
5. Submit these in the lab 4 folder of your class [Github page], either as links or uploaded files. Each group member should post their own copy of the work to their own Lab Hub, even if some of the work is the same for each person in the group.


## Overview
Here are the parts of the assignment

A) [Capacitive Sensing](#part-a)

B) [OLED screen](#part-b) 

C) [Paper Display](#part-c)

D) [Wizard the device](#part-d-wizard-the-device) 

E) [Costume the device](#part-e-costume-the-device)

F) [Record the interaction](#part-f-record)

## The Report
This readme.md page in your own repository should be edited to include the work you have done. You can delete everything but the headers and the sections between the **stars**. Write the answers to the questions under the starred sentences. 

Include any material that explains what you did in this lab hub folder, and link it in the readme.

Labs are due on Mondays. Make sure this page is linked to on your main class hub page.

### Part A
### Capacitive Sensing, a.k.a. Human Banana Interaction

We wanted to introduce you to the [capacitive sensor](https://learn.adafruit.com/adafruit-mpr121-gator) in your kit. It's one of the most flexible input devices we were able to provide. At boot it measures the capacitance on each of the 12 contacts. Whenever that capacitance changes it considers it a user touch. You can attach any conductive material. In your kit you have conductive fabric and copper tape that will work well, but don't limit yourself! In this lab we will use (go?) bananas!

<p float="left">
<img src="https://cdn-learn.adafruit.com/guides/cropped_images/000/003/226/medium640/MPR121_top_angle.jpg?1609282424" height="150" />
<img src="https://cdn-shop.adafruit.com/1200x900/4401-01.jpg" height="150">
<img src="https://post.healthline.com/wp-content/uploads/2020/08/banana-pink-background-thumb-1-732x549.jpg" height="150">
</p>

Plug in the capacitive sensor board with the qwiic connector. Connect your banana's with either the copper tape or the alligator clips (the clips work better). make sure to install the requirements from `requirements.txt`

![](https://media.discordapp.net/attachments/679721816318803975/823299613812719666/PXL_20210321_205742253.jpg?width=1518&height=1139)

I've connected my banana's* to pads 6 and 10. When you run the code and touch a banana the terminal will print out the following

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python cap_test.py 
Banana 10 touched!
Banana 6 touched!
```

*\*Some students have noted that their banana's look noticeably different from the ones presented in this demo. We firmly reject the accusation that these are not in fact banana's but Twizzlers™. Due to the challenges of remote teaching we cannot debug banana's at this time. We suggest you bring these issues up with the university or your local produce representative*

**My demo of the capacitive sensor:**

[![](https://res.cloudinary.com/marcomontalbano/image/upload/v1616886589/video_to_markdown/images/google-drive--1XSGrefj-1_0yi6CXBM2GCBVGjimb_T20-c05b58ac6eb4c4700831b2b3070cd403.jpg)](https://drive.google.com/file/d/1XSGrefj-1_0yi6CXBM2GCBVGjimb_T20/view?usp=sharing "")


### Part B
### OLED screen

We just received some of the small oled screens that we had coped to include in your kit. If you want one feel free to pop into the lab and get one. These don't have colors like the one on the pi but you can move it around on a cable making for more flexible interface design. The way you program this display is almost identical to the pi display. Take a look at `oled_test.py` and some more of the [Adafruit examples](https://github.com/adafruit/Adafruit_CircuitPython_SSD1306/tree/master/examples).

<p float="left">
<img src="https://cdn.sparkfun.com//assets/parts/1/6/1/3/5/17153-SparkFun_Qwiic_OLED_Display__0.91_in__128x32_-01.jpg" height="200" />
<img src="https://cdn.discordapp.com/attachments/679466987314741338/823354087105101854/PXL_20210322_003033073.jpg" height="200">
</p>

**I'm yet to pick up my oled screen :'(**

### Part C
### Paper Display

Here is an Pi with a paper faceplate on it to turn it into a display:

<img src="https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2020Fall/images/paper_if.png?raw=true"  width="250"/>


This is fine, but it can be a bit difficult to lay out a great and user friendly display within the constraints of the Pi. Also, it really only works for applications where people can come and stand over the Pi, or where you can mount the Pi to the wall.

Here is another prototype for a paper display:

<img src="https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2020Fall/images/b_box.png?raw=true"  width="250"/>

It holds a pi and usb power supply, and provides a front stage on which to put writing, graphics, LEDs, buttons or displays.

This design can be made by scoring a long strip of corrugated cardboard of width X, with the following measurements:

| Y height of box <br> <sub><sup>- thickness of cardboard</sup></sub> | Z  depth of box <br><sub><sup>- thickness of cardboard</sup></sub> | Y height of box  | Z  depth of box | H height of faceplate <br><sub><sup>* * * * * (don't make this too short) * * * * *</sup></sub>|
| --- | --- | --- | --- | --- | 

Fold the first flap of the strip so that it sits flush against the back of the face plate, and tape, velcro or hot glue it in place. This will make a H x X interface, with a box of Z x X footprint (which you can adapt to the things you want to put in the box) and a height Y in the back. 

Here is an example:

<img src="https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2020Fall/images/horoscope.png?raw=true"  width="250"/>


Make a paper display for your project that communicates the state of the Pi and a sensor. Ideally you should design it so that you can slide the Pi out to work on the circuit or programming, and then slide it back in and reattach a few wires to be back in operation.
 
**a. Document the design for your paper display.** (e.g. if you had to make it again from scratch, what information would you need?). Include interim iterations (or at least tell us about them).

**"Looks like" prototype:**
Since this piggybank stores only loose change, there could only be 4 potential options for the amount of money being inserted. I have used the capacitive sensor to find out what type of coin is being added. I have also used the rotary encoder for the user to inform the box of how many coins of the current type are being added - I tried making use of the proximity sensor and the accelerometer to automatically detect when a coin is being added, but I was unsuccessful in getting this functionatlity (this is something I will work on for the next iteration). To inform the user of the total amount of money in the bank and the count of each coin, I added 2 relevant buttons. I intend on adding a screen once I am able to get my hands on an oled screen. Here is the first iteration of a rough sketch I made for this box:

<img src="media/sketch.jpg" width="350"/>

Here are photos of what the cardboard prototype look like (it was not my intention to make it look so pet-like):

<img src="media/p1.jpg" width="300"> <img src="media/p2.jpg" width="300"> <img src="media/p3.jpg" width="300">

Updated version:

<img src="media/p4.jpg" width="300">

I taped a small little bag inside the box to grab all the coins that are inserted, such that they don't interfere with the technology that will also lie inside (specifically the pi, the sensors and the buttons). I also cut up a small replaceable door, so that I could easily make any alterations to the pi when necessary. 

**b. Make a video of your paper display in action.**

**"Works like" prototype:**
[![](https://res.cloudinary.com/marcomontalbano/image/upload/v1616886540/video_to_markdown/images/google-drive--1F46lqY5GtjhiOxW4Fa6vqFDQOjOomnpR-c05b58ac6eb4c4700831b2b3070cd403.jpg)](https://drive.google.com/file/d/1F46lqY5GtjhiOxW4Fa6vqFDQOjOomnpR/view?usp=sharing "")

Updated version:
[![](https://res.cloudinary.com/marcomontalbano/image/upload/v1616901944/video_to_markdown/images/google-drive--1lC4jLLxtaO9PB4rdteclrTedkfif8SJL-c05b58ac6eb4c4700831b2b3070cd403.jpg)](https://drive.google.com/file/d/1lC4jLLxtaO9PB4rdteclrTedkfif8SJL/view?usp=sharing "")

**c. Explain the rationale for the design.** (e.g. Does it need to be a certain size or form or need to be able to be seen from a certain distance?)

**"Looks like" prototype:**
I designed this interactive piggybank to be box-like and small, so that it could sit on your desk or in some space and not take up too much room. It does not need to be noticed from a distance, and can easily be placed in any part of your room (whatever you want or are comfortable with). I also intended for the device to not look flashy, such that if a thief were to raid your house, they wouldn't find your precious loose change. The entire device (without any money added) should not weigh a lot because the coins that will be added to the box will end up causing the entire thing to become quite heavy. Therefore, the aim of the design was to create a small, lightweight, non-obstructive box to store all the wires, technology and money that it contains.

### Part D
### Materiality

**Open Ended**: We are putting very few constraints on this part but we want you to get creative.

Design a system with the Pi and anything from your kit with a focus on form, and materiality. The "stuff" that enclose the system should be informed by the desired interaction. What would a computer made of rocks be like? How would an ipod made of grass behave? Would a roomba made of gold clean your floor any differently?

**a. document the material prototype.** Include candidates that were considered even if they were set aside later.

The material prototype that was used was the cardboard box shown above. It had the right shape, structure, weight and feel to it and worked as the best option for my purposes of having an interactive piggybank.

**b. explain the selection.**

There wasn't much of a selection, since the only material I could work with was cardboard. I could have built a purely paper object. However it would not have the required sturdiness that a piggybank ought to have. I did not have any harder materials to work with, such as glass or plastic - though, for a piggybank they would have made better candidates.

### Part 2.

Following exploration and reflection from Part 1, complete the "looks like," "works like" and "acts like" prototypes for your design.

Reiterating:
### Deliverables for this lab are: 
1. Sketches/photos of device designs
1. "Looks like" prototypes: show us what how the device should look, feel, sit, weigh, etc.
3. "Works like" prototypes: show us what the device can do
4. "Acts like" prototypes: videos/storyboards/other means of showing how a person would interact with the device
5. Submit these in the lab 4 folder of your class [Github page], either as links or uploaded files. Each group member should post their own copy of the work to their own Lab Hub, even if some of the work is the same for each person in the group.

**"Acts like" prototype:**
Here is a final video of the entire system in action:
[![](https://res.cloudinary.com/marcomontalbano/image/upload/v1616947789/video_to_markdown/images/google-drive--1E4bfhPOdC_G4UfilI-a64B_zStiX3V2P-c05b58ac6eb4c4700831b2b3070cd403.jpg)](https://drive.google.com/file/d/1E4bfhPOdC_G4UfilI-a64B_zStiX3V2P/view?usp=sharing "")

This is what the inside of the box looks like:

<img src="media/p5.jpg" width="300"> 

These are the items that the box contains (front and back):

<img src="media/p7.jpg" width="300"> <img src="media/p6.jpg" width="300"> 

This is what the board holding all the technology looks like (I made and used this board, so that it would be easy to take out and put back in, rather than having to work on each item within the small box):

<img src="media/p8.jpg" width="600">

For any next iterations of the interactive piggybank, I would make the following changes/improvements:
- Automate the coin adding, so that the user doesn't have to specify the number of coins being added
- Fix irregularities in performance by cleaning up the capacitive sensor connections
- Use a slightly bigger box and enclose all the items more tightly/compactly
- Include a feature that allows you to decrement the amount of coins that are in the bank

