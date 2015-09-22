#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Bismillah
#ONI(c) , Project Ironica
#Version 2.0
#Brashi
#Ref Id: 120
#Dated: 5/8/15
#Ubdus Samad
i = 2
from funcs import *
#==========================================UD============================================
def start_(z):
    if any(i in z for i in do_not):
        speak('Okay sir , i will not do it.')
    elif any(i in z for i in audio):
        speak('Anything for you Sir.')
        subprocess.call(["rhythmbox-client", "--play"]) #rhythmbox START
    elif 'vlc' in z:
        speak('Starting vlc media player for you sir!')
        subprocess.Popen(['vlc'])
    elif 'rhythmbox' in z:
        speak('rhythm box started sir')
        subprocess.Popen(['rhythmbox'])
    elif 'notepad' in z or 'gedit' in z:
        speak('There you go sir')
        subprocess.Popen('gedit')
    elif 'firefox' in z or 'web' in z or 'browser' in z:
        speak('Executing firefox sir')
        subprocess.Popen('firefox')
        time.sleep(3)
        speak('There you go sir')
    elif 'home' in z or 'computer' in z:
        speak('File manager navigated to home sir')
        subprocess.Popen('nautilus')
    elif 'uget' in z or 'download manager' in  z:
        speak('Starting Uget sir')
        subprocess.Popen('uget-gtk')
    elif 'ik' in z:
        subprocess.Popen(['vlc','/home/syed/Music/ik.xspf'])
    else:
        speak('please specify what do you want to start sir')
        
def stopcmd(z):
    if any(i in z for i in audio):
        subprocess.call(["rhythmbox-client", "--pause"])#rhythmbox STOP
    elif 'vlc' in z:
        subprocess.call(['killall','vlc'])
    elif 'rhythmbox' in z:
        subprocess.call(['killall','rhythmbox'])
    elif 'notepad' in z or 'gedit' in z:
        subprocess.call(['killall','gedit'])
    elif 'firefox' in z or 'web' in z or 'browser' in z:
        subprocess.call(['killall','firefox'])
    elif 'home' in z or 'computer' in z:
        subprocess.call(['killall','nautilus'])
    elif 'uget' in z or 'download manager' in z:
        subprocess.call(['killall','uget-gtk'])
    else:
        speak('please specify what do you want to stop sir')
#------------------------------------Main()--------------------------------
def ai(z):
    o_l = 0
    if 'google' in z or 'search' in z:
        google(z)
    elif any(i in z for i in w_n):
        rnd = random.randint(-1,6)
        speak(welcome_notes[rnd + 1])
    #--------------------------------------
    elif any(i in z for i in query):
        #cmd_cat = "qry"
        speak("You want to know something! Right?")
        time.sleep(2)
        if any(i in z for i in about_me_cmds):
            speak(about_me)
    #------------------------------------
    elif any(i in z for i in sett_):
        #cmd_cat = "make"
        set_(z)
    #-------------------------------------
    elif any(i in z for i in show_):
        #cmd_cat = "sho"
        speak("You want to see something.")
        time.sleep(1.5)
        if any(i in z for i in tame):
            dt = 'Today is '+time.ctime()
            speak(dt)
        if any(i in z for i in contacts):
            pass
    #---------------------------------------
    elif any(i in z for i in start):
        #cmd_cat = "start"
        start_(z)
        pass
    #---------------------------------
    elif any(i in z for i in live_ques):
        if any(i in z for i in alive):
            speak("Yes sir i am good and ready for service! :)")
    elif any(i in z for i in stop_):
        stopcmd(z)
    #----------------------------------------------------------------------------------------------------------------------------------------
    else:                                     #Else carries Some exceptional funcs too!
        #cmd_cat = "else"
        els(z)

while i>1:
    if i == 2:
        speak('Brashi At your service Sir')
    r_cmd = raw_input('|>>> At your service:')
    cmd = ' '+r_cmd.lower()+' '
    ai(cmd)
    #break
    i = i + 1
    if cmd == "e":
        break


#--------------------
