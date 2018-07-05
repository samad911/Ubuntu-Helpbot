#ONI(c) | Project Red Queen
#ONI Corporation Limited
#VAR-CUM-STT Engine for Project Red Queen
#December 9 2016
from sys import byteorder
from array import array
from struct import pack
import pyglet
import time
import speech_recognition as sr
import pyaudio
import wave
from os import path

import sounddevice as sd

fs=96000
duration = 5  # seconds
my = sd.rec(duration * fs, samplerate=fs, channels=2)
sd.wait()

sd.play(my,fs,blocking='False')
