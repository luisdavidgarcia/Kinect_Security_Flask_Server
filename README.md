# Kinect_Security_Flask_Server

A Flask Web App that permits the user use their Xbox 360 Kinect as a survilence camera for their home, room, or general purpose area. 

<img src="KinectApp.png">

<h2>Technologies</h2>
<ul>
  <li>Flask</li>
  <li>Python</li>
  <li>libfreenect Source Code for Xbox 360 Kinect</li>
  <li>OpenCV2 </li>
  <li> Kinect USB Adapater </li>
  <li> html/css </li>
</ul>  

<h2>How to Run</h2>
<ul>
  <li>Connect Kinect USB Adapter to your Kinect and your Computer/Laptop</li>
  <li>Install the libfreenect software and OpenCV2 from this <a href="https://naman5.wordpress.com/2014/06/24/experimenting-with-kinect-using-opencv-python-and-open-kinect-libfreenect/">website<a/>. </li>
  <li>Install Flask with <code>pip3 install flask</code></li>
  <li>Clone this repository</li>
  <li>Run <code>python3 app.py</code> in your terminal to start Flask app</li>
  <li>Open the link provided in your terminal after you run the Flask app to go the web app where you will see you're Kinect streaming real-time footage.</li>
</ul>  


<h2>Motivation for the Project</h2>

Over these past two weeks, I got the opportunity to learn how to turn my Xbox 360 Kinect into a web cam. 

I first opted for a Raspberry Pi with a camera module, but my Pi only has 1 GB of ram, so the footage would crash and look like this:

<video src="kinectRecording.mp4" />

https://user-images.githubusercontent.com/87344382/140658297-47862c56-2efb-45c8-916f-08e239428a72.mp4

However, I then remembed the Kinect being used in many applications in robotics before for guided assistance and 3D scanning.

So I thought why notstart using it as a security camera to observe when I am away from home. I got to working as soon as the Kinect USB adapter came in, but it was difficult finding any information on what libraries to install to have the Kinect working properly, but thankfully my answers were solved when I found this <a href="https://naman5.wordpress.com/2014/06/24/experimenting-with-kinect-using-opencv-python-and-open-kinect-libfreenect/">website<a/>.

Although the website seems outdated, the only change that must be made is when installing the wrappers to program the Kinect with Python the wrappers must be installed with Python3 or the appropriate version of Python you have installed or else the programs you run will not work properly. After installing OpenCV, I made my Flask App, which was just simple HTML, but when it came to using Flask I spent a whole four days learning how to have the video from the Kinect be streamed from the HTML index file I made.
  
<img src="FlaskRunning.png">  
  
Yet, I found a <a href="https://www.youtube.com/watch?v=vF9QRJwJXJk">tutorial</a> where the host streams live footage from his web cam onto a flask app. The only difference is I need to have the footage stream form the Kinect not my web cam. 
  
To only access the Kinect I learned about the “/dev/video*” inputs in Ubuntu, which denote cameras that are plugged in/installed.

Moreover, to access my Kinect’s camera I just had use the videoCapture function to attain the footage, then I use the read command to process a frame, turn it into a JPEG format, and encode it to bytes. 

I have to capture each frame in order to have the video output in web page (the HTML index file) and using Flask I create another route called “video,” but the route gives a response similar to how an API works because the response returns each frame of the footage as JPEG image, so that the video can properly display in index HTML file.  

Here is a proper demontration of it working, but I just needed to center the video footage to the center of the screen using CSS: 
  
<video src="raspberryPiweakCamera.mp4" />  
  
https://user-images.githubusercontent.com/87344382/140658404-71a82010-1b0e-4d37-bb18-b2d7a2769631.mp4


