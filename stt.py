#!/usr/bin/env python3
#STT Engine For Red Queen
#ONI Corporation Limited

import speech_recognition as sr

# obtain path to "english.wav" in the same folder as this script
from os import path
#AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "english.wav")
#AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "french.aiff")
#AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "chinese.flac")

# use the audio file as the audio source
def listen(audio_file):
    #Stt engine activator
    AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), audio_file)
    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source) # read the entire audio file
# recognize speech using Google Speech Recognition
    try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
        return r.recognize_google(audio, key="AIzaSyAcalCzUvPmmJ7CZBFOEWx2Z1ZSn4Vs1gg")
    except sr.UnknownValueError:
        return None
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

