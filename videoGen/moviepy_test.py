#!/usr/bin/env python
# -*- coding: utf-8 -*-

#moviepy test
from moviepy.editor import *
import uuid

def makeVideo(input=[], imgfilename=""):

	video1 = VideoFileClip('static/video/fire_explosion_01.mp4')
	video2 = VideoFileClip('static/video/IphonePreview.mp4')
	image1 = ImageClip(imgfilename) #check om der er en fil her og om det er en png og lav alternativ composite_final


	#indsæt form input logik som afgør videosammensætning
	if input[0] == "Banking":

		video_final = concatenate_videoclips([video1,video2])

	else:
		
		video_final = concatenate_videoclips([video2,video1])	


	composite_final = CompositeVideoClip([video_final, image1]).set_duration(video_final.duration)	

	#logo submit til db og overlay.
	extension = '.mp4'
	videoname = str(uuid.uuid4()) + extension

	composite_final.write_videofile('static/video/generated/' + videoname, fps=25)

	return videoname