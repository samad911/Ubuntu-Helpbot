#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Bismillah
#ONI(c) , Project Red Queen
#Version 2.0
#Red Queen
#Ref Id: 150
#Dated: 5/8/15
#Ubdus Samad
i = 2
hot_word='red queen'
#rec_len_thresh=7#Seconds

from funcs import *
from var import *
from stt import *
from classifier import *
import os
#------------------------------------Main()-------------------------------

while i>1:
    if i == 2:
        speak('At your service Sir')
        time.sleep(1.5)
    #This is the recognizer part
    print("Please speak a word into the microphone:")
    while 1:
        bp=pyglet.resource.media('beep.wav')
        bp.play()
        record_to_file('demo.wav')#,rec_len_thresh)
        #music = pyglet.resource.media('demo.wav')
        r_cmd=str(listen('demo.wav'))
        print r_cmd
        os.remove('demo.wav')
        if hot_word in r_cmd.lower():
            music = pyglet.resource.media('ding.wav')
            music.play()
            break
        elif r_cmd == None:
            speak('Kuch gadbad hai')
    #And here it ends
    #r_cmd = raw_input('|>>> At your service:')
    cmd = ' '+r_cmd.lower()+' '
    ai(cmd)
    #break
    i = i + 1
    if cmd == "e":
        break


#--------------------
