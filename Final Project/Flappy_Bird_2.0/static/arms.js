const socket = io();
socket.on('connect', () => {});

setInterval(() => {
      socket.emit('ping-arms', 'dat')
      }, 100)

socket.on('disconnect', () => {
      console.log('disconnect')
      });

const webcamElement = document.getElementById('webcam');
const webcam = new Webcam(webcamElement, 'user');

// Create our 'main' state that will contain the game
var mainState = {

   this.gameOverFlag = false;

preload: function() {
            // This function will be executed at the beginning
            // Load the bird sprite
            game.load.image('bird', 'static/assets/bird.png');
            game.load.image('pipe', 'static/assets/pipe.png');
            game.load.image('playAgain', 'static/assets/playagain.png');

            webcam.start()
               .then(result =>{
                     console.log("webcam started");
                     })
            .catch(err => {
                  console.log(err);
                  });
         },

create: function() {
           // This function is called after the preload function
           // Change the background color of the game to blue
           game.stage.backgroundColor = '#71c5cf';

           // Set the physics system
           game.physics.startSystem(Phaser.Physics.ARCADE);

           // Display the bird at the position x=100 and y=245
           if (this.bird) {
              this.bird.destroy();
           }
           this.bird = game.add.sprite(100, 245, 'bird');

           // Add physics to the bird
           // Needed for: movements, gravity, collisions, etc.
           game.physics.arcade.enable(this.bird);

           // Add gravity to the bird to make it fall
           this.bird.body.gravity.y = 700; 

           const imageScaleFactor = 0.50;
           const flipHorizontal = false;
           const outputStride = 16;

           async function estimatePoseOnImage(imageElement, jumpFunc, bird) {
              this.bird = bird;
              const net = await posenet.load();

              // load the posenet model
              const pose = await net.estimateSinglePose(imageElement, imageScaleFactor, flipHorizontal, outputStride);

              console.log(pose);

              if (pose.keypoints[0].position.y > pose.keypoints[9].position.y && pose.keypoints[0].position.y > pose.keypoints[10].position.y) {
                 console.log("attempted jump");
                 jumpFunc();
              } else {
                 console.log("so sad too bad");
              }

              return pose;
           }

           if (!gameOverFlag) {
              setInterval(() => {
                    const pose = estimatePoseOnImage(webcamElement, this.jump, this.bird);
                    }, 800);
           }

           // Create an empty group
           this.pipes = game.add.group(); 

           this.timer = game.time.events.loop(1500, this.addRowOfPipes, this); 

           this.score = 0;
           this.labelScore = game.add.text(20, 20, "0", 
                 { font: "30px Arial", fill: "#ffffff" });   
        },

update: function() {
           // This function is called 60 times per second
           // It contains the game's logic
           // If the bird is out of the screen (too high or too low)
           // Call the 'restartGame' function
           if (this.bird.y < 0 || this.bird.y > 490)
              this.gameOver();

           game.physics.arcade.overlap(
                 this.bird, this.pipes, this.gameOver, null, this);

           game.scale.pageAlignHorizontally = true;
           game.scale.refresh();
        },

jump: function() {
         // Add a vertical velocity to the bird
         this.bird.body.velocity.y = -250;
      },

addOnePipe: function(x, y) {
               // Create a pipe at the position x and y
               var pipe = game.add.sprite(x, y, 'pipe');

               // Add the pipe to our previously created group
               this.pipes.add(pipe);

               // Enable physics on the pipe 
               game.physics.arcade.enable(pipe);

               // Add velocity to the pipe to make it move left
               pipe.body.velocity.x = -200; 

               // Automatically kill the pipe when it's no longer visible 
               pipe.checkWorldBounds = true;
               pipe.outOfBoundsKill = true;
            },

addRowOfPipes: function() {
                  // Randomly pick a number between 1 and 5
                  // This will be the hole position
                  var hole = Math.floor(Math.random() * 5) + 1;

                  // Add the 6 pipes 
                  // With one big hole at position 'hole' and 'hole + 1'
                  for (var i = 0; i < 8; i++)
                     if (i != hole && i != hole + 1 && i != hole - 1)
                        this.addOnePipe(400, i * 60 + 10);

                  this.score += 1;
                  this.labelScore.text = this.score;
               },

gameOver: function() {
             this.gameOverFlag = true;
             webcam.stop();
             game.state.start('StateOver');
          }
};

var StateOver={    
create:function()
       {
          //add a sprite to be used as a play again button
          this.playAgain = game.add.sprite(game.width/2,game.height/2,'playAgain');
          //center the button image
          this.playAgain.anchor.set(0.5,0.5);
          //enable for input
          this.playAgain.inputEnabled = true;
          //add an event listener
          this.playAgain.events.onInputDown.add(this.restartGame,this);
       },

restartGame:function()
            {
               //restart the game by starting stateMain
               game.state.start('main');
            }
}

// Initialize Phaser, and create a 400px by 490px game
var game = new Phaser.Game(400, 490);

// Add the 'mainState' and call it 'main'
game.state.add('main', mainState);
game.state.add('StateOver', StateOver);

// Start the state to actually start the game
game.state.start('main');

