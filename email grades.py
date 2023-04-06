# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 23:22:48 2023

@author: Tom
"""

from canvasapi import Canvas
from datetime import datetime, timedelta


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


#first we get all users for a course
users = course.get_users(enrollment_type=['student'])


start_time = datetime.now() - timedelta(days=1)
end_time = datetime.now()
grade_changes = {}
#then we get all grade changes for the past 24 hours
for user in users:
    print(user)
    grade_changes[user.id] = (user.get_grade_change_events_for_student())
    #grade_changes.append(user.get_grade_change_events_for_student(start_time = datetime.now() - timedelta(days=1), end_time = datetime.now()))

#then send email
for user in users:
    profile = user.get_profile()
    email = profile.email
    msg = "Here are the changes in grades from the last 24 hours" + grade_changes[user.id]
    
    #send email somehow 
    #needs a SMTP server perhaps
    #https://realpython.com/python-send-email/#sending-your-plain-text-email