import os 
from flask import Flask, render_template, Response 
#from kinect import Kinect360
import cv2

app = Flask(__name__)
#deviceNumber depends on the source of your video camera
deviceNumber = 1
camera = cv2.VideoCapture(deviceNumber)

@app.route('/')
def index():
	return render_template('index.html')

def get_frames():
	while 1:
		success,frame=camera.read()
		if not success:
			break
		else:
			ret,buffer = cv2.imencode('.jpg',frame)
			frame=buffer.tobytes()
		yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n'+ frame + b'\r\n')


#def gen(Kinect360):
#	while 1:
#		frame = Kinect360.get_video()
		
#		yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n'+ frame + b'\r\n\r\n')

@app.route('/video')
def video():
	return Response(get_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
	app.run(host='0.0.0.0',threaded=True)

