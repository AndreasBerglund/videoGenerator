#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web
import os
import random
import uuid
from videoGen import moviepy_test

render = web.template.render('templates/')

urls = (
        '/', 'index'
        )

class index:

    def GET(self):

        name = 'navnenavne'
        return render.index(name)


    def POST(self):
    	form = web.input(industry="none", logo = {})
    

    	#file png
    	print form.logo
    	web.debug(form['logo'].filename) # This is the filename
        web.debug(form['logo'].value) # This is the file contents
        web.debug(form['logo'].file.read()) # Or use a file(-like) object


        ####WRITE TO SERVER #####
	extension = os.path.splitext(form['logo'].filename)[1]
	
	
	input_file = form['logo'].file
	imagename = uuid.uuid4()
	file_path = os.path.join('', '%s.png' % imagename)

	output_file = open(file_path, 'w')

	input_file.seek(0)

	while 1:
		data = input_file.read(2<<16)
		if not data:
			break
		output_file.write(data)
	output_file.close()
    	####WRITE TO SERVER#####

    	videoname = moviepy_test.makeVideo([form.industry], file_path)
    	name = "<video controls autoplay><source src='/static/video/generated/"+ videoname + "'type='video/mp4'></video>"


    	return render.index(name)    


if __name__ == "__main__":
    app = web.application(urls,globals())
    app.run()



#inkluder video merger
#to sider = en input og en post side. Pa post siden kan man gøre det forfra og dele/downloade.
#maske noget upload to youtube funktion sa vi ikke skal hoste alt.  ==== popup der siger login og uploader fil.

