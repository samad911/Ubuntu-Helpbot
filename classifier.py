#Classifier Engine For Project Red Queen
#ONI Corporation Limited
from funcs import *
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
