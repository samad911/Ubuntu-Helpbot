# Ubuntu-Helpbot
A simple help bot for Linux based operating systems. (Designed in Ubuntu).

It can run programs, tell you time , play/stop/pause music , increase/dec.. volume etc by just coupling the command with the hot word.
e.g *Red Queen play some music*

The program is not Cross Platform , but you are welcome to modify it's commands for Windows or Mac, as it's not very difficult since you just have to change the commands which are send to the subprocess function.

# Dependencies:

Python:
	
	alsaaudio , SpeechRecognition , pyaudio , pyglet

	You can install alsaaudio by typing this in the teriminal:

	sudo apt-get install alsaaudio and similarly all the above dependencies.

Linux:
	
	Espeak: sudo apt-get install espeak

# Description
It can do other cool stuff but it is in it's Beta form so it lags some stuff , im a loking forward to people who can help me building the program better.
Some to the abilities of the program are still in development but little of it's code is still present , so if you get a akward looking function in the program which is of no use please ignore it cause it might be in it's beta stage more or less it will have a UD  comment in it for example the directory is not fully functional yet.'

Some of the cool tings it can do is to start music player by just saying *read queen go music* or firefox by just saying *red queen go firefox*.
You can use give it instructions in natural language and it will understand it like: *run vlc* or *start vlc* or *start the freaking vlc*

# Usage:

* There are many ' .dat '  extension file imports in this program so  you've got to modify their path in the funcs module
* Put all three ' .py'  extension files together in same folder.
* Run `red_queen.py` and say *red queen hello*. (Remember **red queen** is to be said at every command as it's the hot word.)
* I can't tell you all the commands (*Though they are in natural language and fairly simple*), so you've got to see the program for how all the commands work.
* You can change the hot word by changing the `hot_word` variable in *red_queen.py*.


# Feedback:
If you have any further problems or constructive criticism please mail me at ubdussamad@gmail.com
