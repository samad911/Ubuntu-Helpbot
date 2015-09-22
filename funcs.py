import time
import subprocess
import random
import os
import alsaaudio #You need to add this little program for working with audios or you'll see error
i1 = open('/home/syed/ironica_commands.dat', 'r')#Commands To be Checked
i2 = open('/home/syed/return_notes.dat', 'r') #Return Notes
i3 = open('/home/syed/sub_cmd.dat', 'r') #Return Notes
i4 = open('/home/syed/dir.dat').read().lower().split()
#----------------------------------------------------
split_cmd = i1.read().split('&')#Splitting Commands to be checked
splitted_notes = i2.read().split('&')#Splitting Commands to be checked
split_sub_cmd = i3.read().split('$') #SpllitingSub commands to check
#splitted_contacts = i4.read()
#-----------------------COMMANDS---------------------
nums =  split_cmd[0].split(',')
time_ = split_cmd[1].split(',')
start = split_cmd[2].split(',')
sett_ = split_cmd[3].split(',')
w_n = split_cmd[4].split(',')
query = split_cmd[5].split(',')
show_ = split_cmd[6].split(',')
about_me_cmds = split_cmd[7].split(',')
offensive_commands = split_cmd[8].split(',')
okay_cmds = split_cmd[9].split(',')
live_ques = split_cmd[10].split(',')
alive  = split_cmd[11].split(',')
tareef = split_cmd[12].split(',')
stop_ = split_cmd[13].split(',')
#---------------------RETURN NOTES------------------
offensive_notes  = splitted_notes[3].split(',')
welcome_notes = splitted_notes[0].split(',')
sorry_notes = splitted_notes[1].split(',')
about_me = splitted_notes[2]
leave = splitted_notes[5].split(',')
welcome_return = splitted_notes[4].split(',')
#----------------------Sub Commands-------------
audio = split_sub_cmd[0].split(',')
tame = split_sub_cmd[1].split(',')
thanks = split_sub_cmd[2].split(',')
decrease_ = split_sub_cmd[3].split(',')
increase_ = split_sub_cmd[4].split(',')
do_not = split_sub_cmd[5].split(',')
#-----------------------------------------------------
cn = ''
#------------------------------------------------------
contacts = []
contacts = i4
b = 0
while b != len(i4):
    i5 = i4[b]
    contacts[b] = i5[:i5.index('-')]
    b = b + 1
    contacts = contacts
def google(z):
    a = z[7:].split(' ')
    s = []
    for i in range(0,len(a)):
        n = '+'+a[i]
        s.append(n)
    search = str(''.join(map(str, s)))
    o = 'googling'+ z[7:]
    speak(o)
    i ='https://www.google.co.in/search?q=' + search[2:len(search)-1]
    subprocess.Popen(['firefox',i])
def speak(z):
    subprocess.Popen(['espeak',z])
def notify(message):
    subprocess.Popen(['notify-send', message])
    return
def increase_any(z):
    if 'vol' in z or 'volume' in z or 'louder' in z:
        speak('I have increased the system volume by 10% sir,')
        subprocess.call( "amixer -D pulse sset Master 10%+", shell=True ) #Increase volume by 10%
    elif 'birghtness' in z or 'screen' in z:
        subprocess.call(['xbacklight','-inc 10'])
def decrease_any(z):
    if 'vol' in z or 'volume' in z:
        speak('I have reduced the system volume by 10% sir,')
        subprocess.call( "amixer -D pulse sset Master 10%-", shell=True ) #Increase volume by 10%
    elif 'birghtness' in z or 'screen' in z:
        subprocess.call(['xbacklight','-dec 10'])
def set_(z):
    if "alarm" in z:
        x = 0
        speak("Setting alarm...")
        if any(i in z for i in nums):
            print "You have given me the numbers"
            for i in z:
                if i in nums:
                    time_[x] = int(i)
                    x = x + 1
                else:
                    pass
            i = str(''.join(map(str, time_)))
            so = "The alarm is set for"+i+"Hrs."
            speak(so)
        else:
            "Please specify the time Sir!"
    elif 'volume' in z or 'vol' in z:
        vol = [0,0]
        x = 0
        if any(i in z for i in nums):
            print "You have given me the numbers"
            for i in z:
                if i in nums:
                    vol[x] = int(i)
                    x = x + 1
                else:
                    pass
            f_vol = int(''.join(map(str, vol))) #Volume Number HUSHHHHHHH..............
            m = alsaaudio.Mixer()   # defined alsaaudio.Mixer to change volume
            m.setvolume(f_vol+1) # set volume
            so = "The Volume is at:",f_vol,"%"
            print so
            speak('Volume numbers changed as instructed sir')
        else:
            "Please specify the Volume Numbers Sir!"
    elif 'count upto' in z:
        count = [0,0,0,0,0,0]
        #UD Please refer to github for updates on development of this sub-sub-fuction
#=====================================================================================
def els(z):
    if any(i in z for i in offensive_commands):
        rnd = random.randint(0,10)
        speak(offensive_notes[rnd])
    elif 'so' in z:
        speak("So what Sir?")
    elif any(i in z for i in okay_cmds):
        speak("Okay!")
    elif 'exit' in z or 'leave' in z or 'out' in z:
        speak('Do you wanna leave sir? hit yes or no')
        ask = raw_input('Do you wanna leave sir? (y/n):')
        if ask == "y" or ask == "ie":
            rnd = random.randint(-1,4)
            speak(leave[rnd + 1])
            exit()
        else:
            speak("Sorry, Sir i thought you wanted to leave, i might be Malfunctioning!")
    elif any(i in z for i in tareef):
        speak("Thanks It was ver Nice Of you!")
    elif 'mute' in z or 'unmute' in z or 'shutup' in z:
        subprocess.call( "amixer -D pulse set Master 1+ toggle", shell=True )
        speak("System Volume unMuted Sir")
    elif any(i in z for i in thanks):
        rnd = random.randint(0,4)
        speak(welcome_return[rnd])
    elif any(i in z for i in decrease_):
        decrease_any(z)
        pass
    elif any(i in z for i in increase_):
        increase_any(z)
        pass
    elif any(cn in z for cn in contacts):
        print cn
        if 'contact' in z:
            pass
            #for any(i in z for i in contacts):
             #   return i
    else:
        rnd = random.randint(0,5)
        speak(sorry_notes[rnd])
