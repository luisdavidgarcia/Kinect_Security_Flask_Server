#import the necessary modules
import freenect
import cv2
import numpy as np
 

class Kinect(object):
	#function to get RGB image from kinect
	def get_video(self):
		array,_ = freenect.sync_get_video()
		array = cv2.cvtColor(array,cv2.COLOR_RGB2BGR)
		return array
	#function to gather frames	
	def process_frames(self):
		frame = self.get_video()
		show_frame = cv2.imshow('RGB image',frame)
	#use this function to have frames show as a video
	def play_video_save_images(self):
		count = 0
		while 1:
			video = self.process_frames()
			# quit program when 'esc' key is pressed
			k = cv2.waitKey(5) & 0xFF
			print("Image" + str(count) + " saved")
			file = "pictures/img" + str(count) + ".jpg"
			cv2.imwrite(file, self.get_video())
			count += 1
			if k == 27:
				break        
	#use this function to just play video
	def play_video(self):
		while 1:
			video = self.process_frames()
			k = cv2.waitKey(5) & 0xFF
			if k == 27:
				break


#create a kinect object
kinect1 = Kinect()

#start the video
kinect1.get_video()

if __name__ == "__main__":
        kinect1.play_video()
        
