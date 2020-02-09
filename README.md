# CiscoBots 

A fun, interactive 2-player sumo bot game with user-customisable maps!  

## How we built it
2 Robot Cars with Raspberry Pi 3 controlled using Wi-Fi. A simple game UI was built using Python and OpenCV

## Challenges we ran into
At first, we tried to use the Xbox One Kinect camera and depth sensor for the detection and tracking of bots. Unfortunately, setting up freenect2 library for integration with Python OpenCV proved to be a lot more difficult than we expected and as a result, we had to change our plan halfway through the project and switch to a less ideal webcam for object recogntion and motion tracking. 

In addition, we were trying to integrate the Cisco Webex facial recognition API to detect changes in the emotions of the player and make the game more interactive by penalising or rewarding the players (i.e. the opponent bot slows down if a player manages to make his/her opponent laugh). We unfortunately ran out of time and had to settle with a simple sumo robot game. 

## What we learned

A lot. For the two of us in the team, it was our first Hackathon. 

## What's next for CiscoBots

Integration of Cisco Facial Recognition API with the game UI

## Built with 

Python, OpenCV, Raspberry Pi 3 
