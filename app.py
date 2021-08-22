import os 
from flask import Flask, render_template

# import camera driver
#if os.environ.get('CAMERA'):
 #   Camera = import_module('camera_' + os.environ['CAMERA']).Camera
#else:
from kinect import Kinect360 

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

#kinect1 = Kinect360()
#kinect1.play_video_save_images()

#def gen(Kinect360):
#	while 1:
#		frame = Kinect360.get_frames()
#		yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n'+ frame + b'\r\n\r\n')

#@app.route('/video_feed')
#def video_feed():
#	return Response(gen(Kinect360()), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
	app.run(host='0.0.0.0',threaded=True)

