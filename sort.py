# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 20:31:57 2023

@author: Tom
"""
from canvasapi import Canvas

#MAIN
# Canvas API URL
COURSE_ID = 15293
API_URL = "https://ursinus.instructure.com"
# Canvas API key
API_KEY = "6723~A2KTPfsPob1ZYugZg3xsrJWaA94bathpwkDemhIyUcZNNGMiTekg6CNtoiFAVtCW"

# Initialize a new Canvas object
canvas = Canvas(API_URL, API_KEY)
# Grab course 123456
course = canvas.get_course(COURSE_ID)