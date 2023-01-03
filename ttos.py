# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 15:53:06 2023

@author: Jayesh
"""

import pyttsx3

'''
txt = pyttsx3.init()
txt.say('Hi, my name is jayesh dharpawar, i am from jalgaon')
txt.runAndWait()
'''
txt_speech = pyttsx3.init()
ro = open('C:\\Users\\Jayesh\\Desktop\\tts.txt','r')
re = ro.read()
ro.close()
txt_speech.save_to_file(re, 'C:\\Users\\Jayesh\\Desktop\\tts.txt.mp3')
txt_speech.setProperty('rate', 150)
txt_speech.setProperty('volume', 1)
# txt_speech.say(re)
txt_speech.runAndWait()
