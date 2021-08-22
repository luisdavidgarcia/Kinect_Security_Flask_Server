#import the necessary modules
import freenect
import time
import cv2
import numpy as np

class Kinect360(object):
	#function to get RGB image from kinect
	def get_video(self):
		array,_ = freenect.sync_get_video()
		array = cv2.cvtColor(array,cv2.COLOR_RGB2BGR)
		ret, array = cv2.imencode('.jpg',array)
		return array 
		
	#function to gather frames	
	def get_frames(self):
		image = self.get_video()
		ret, jpeg = cv2.imencode('.jpg',image)
		data = []
		data.append(jpeg)
		return data
		
	#use this function to have frames show as a video
	def play_video_save_images(self):
		count = 0
		while 1:
			frame = self.get_video()
			#show_frame = cv2.imshow('RGB',frame)
			# quit program when 'esc' key is pressed
			#print("Image" + str(count) + " saved")
			file = "static/img" + str(count) + ".jpg"
			cv2.imwrite(file, self.get_video())
			count += 1
			k = cv2.waitKey(5) & 0xFF
			if k == 27:
				break        
	
	#use this function to just play video
	def play_video(self):
		while 1:
			frame = self.get_video()
			show_frame = cv2.imshow('RGB',frame)
			# quit program when 'esc' key is pressed
			#img = cv2.imencode('.jpg',frame)[1].tobytes()
			#yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + img + b'\r\n')
			#time.sleep(0.1)
			k = cv2.waitKey(5) & 0xFF
			if k == 27:
				break
		cv2.destroyAllWindows()

#create a kinect object
#kinect1 = Kinect360()

#while 1:
#	kinect1.play_video()
#	k = cv2.waitKey(5) & 0xFF
#	if k == 27:
#		break
        
