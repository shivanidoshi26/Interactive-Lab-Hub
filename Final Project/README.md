# Final Project

Using the tools and techniques we learned in this class, Ritika Poddar (rp477) and I (sgd73) designed, prototyped and tested an interactive device: Flappy Bird 2.0!
 
## Description

Flappy Bird is a mobile game developed by Vietnamese video game artist and programmer Dong Nguyen, under his game development company dotGears. The game is fairly simple and merely requires the player to control a bird on the screen. The goal of the game is to navigate the bird through a sort of obstacle course of green pipes. You have to try and get as far as you possibly can without hitting the green pipes or going out of the bounds of the screen (i.e. going too high or too low). 

While this game sounds simple, it was always very tricky to get a high score and perform well - people have spent hours practicing and trying to get the motions correct. The game was discontinued due to the violent reactions people had when they lost. It was such an addicting game and it really pushed people to perform (or try to perform) well. The game is still available on some websites and some off-brand mobile apps.

Our goal for this final project was to replicate the game on a web application, but elevate the methods one could use to maneuver the bird. Ordinarily, a person would repeatedly tap on the mobile screen to keep the bird afloat, or repeatedly press the spacebar of your computer in the case of the web app. We decided to alter that and make use of some of the cool technology we were provided in this course. 

We, therefore, implemented 3 modes in our project: joystick, accelerometer and arms mode. The joystick mode is the easiest, accelerometer a bit tougher and arms the hardest. The following storyboard depicts a classic interaction:

<p align="center">
 <img src="imgs/storyboard.png"/>
</p>

Note: our intention with this project was not to trigger anyone's prior negative experiences with the game, but rather introduce slightly modified versions of the original and hopefully provide a fun, lively and interactive experience!

## Documentation of Design Process

The following sections detail out all the prototyping, coding, reflecting, demoing and so on that we went through to create this amazing rendition of the game.

## Archive of Everything

For extremely detailed instructions about how to get set up with the right packages, code and environment, please refer to the README in the Flappy_Bird_2.0 directory within this repository. Here is the link to the folder: https://github.com/shivanidoshi26/Interactive-Lab-Hub/tree/Spring2021/Final%20Project/Flappy_Bird_2.0.

Our ultimate goal for the physical design of the device was for it to be very simple. Since we were building up a game, we wanted all the technology to be close and well-connected. As we built a web application, one wouldn't be able to access the game without a computer. Having kept that in mind, we did our best to simplify the container for the rest of the technology. One of most important things we needed to keep in mind with our design was to orient the devices the right way, because our solution works with very specific directions and movements with the tech. 

If we had more experience and time to make use of the resources in the Maker Lab, we would've encased our devices in something more sturdy instead of cardboard. However, given the time and resource constraints we had, this is what we had to settle for.

Our initial design was exceedingly simple and, as you can see, there are some flaws with it. The accelerometer was not as handheld as we would've liked it to be and there's nothing really exciting about this set up.

<p align="center">
 <img src="imgs/design1.jpg" height=400/>
</p>

The second iteration was much better as it hid the raspberry pi as well, and the accelerometer was put in a piece of tech that could actually be held in your hand:

<p align="center">
 <img src="imgs/design2.jpg" height=400/>
</p>

## Video Demos

Since we didn't want to put anyone's health at jeopardy by having them demo the application, we decided to show you how it can be used ourselves:

[![](https://res.cloudinary.com/marcomontalbano/image/upload/v1620924087/video_to_markdown/images/google-drive--1ma2-HkcZKHPzy7PB_bqO0nm2dztGvdqr-c05b58ac6eb4c4700831b2b3070cd403.jpg)](https://drive.google.com/file/d/1ma2-HkcZKHPzy7PB_bqO0nm2dztGvdqr/view "")

## Reflections

4. Reflections on process (What have you learned or wish you knew at the start?)

## Teams

Ritika Poddar (rp477) and I decided to work together for the entirety of this project. The effort we both put in was extremely equal and we're both very happy with how we've worked as a team (for not only this project, but most of them throughout the semester). Specifically:
- Ritika started us off and implemented the basic infrastructure of the game.
- I cleaned up the UI and integrated all the components of the web application together to make a smooth web interaction.
- We figured out how to implement the accelerometer appropriately. 
- Ritika got the joystick working, which was quite easy to figure out once we'd figured out the accelerometer. 
- Ritika played around with posenet and got a basic version with the pi cam working - we decided to scrap using the pi cam due to issues with major delays and slowness.
- We collectively figured out how to instead perform all the arms code browser-side - for this we needed to gain access to the computer's web camera and use that input to process the subsequent actions. A big thanks to David Goedicke for staying on call for nearly an hour helping us figure out how to get the web cam working!
- We finally got arms to work pretty cleanly and process the input at a fairly normal rate.
- I reorganized the UI and made last-minute touches and improvements.

The documentation and code for our final project is the same on both hers and my repository. Here is a link to her final project repository, in any case: https://github.com/Rpoddar1953/Interactive-Lab-Hub/tree/Spring2021/Final%20Project.
