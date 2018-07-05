from var import *
from stt import *
from pydub import AudioSegment


def detect_leading_silence(sound, silence_threshold=-50.0, chunk_size=512):
    '''
    sound is a pydub.AudioSegment
    silence_threshold in dB
    chunk_size in ms

    iterate over chunks until you find the first one with sound
    '''
    trim_ms = 0 # ms
    while sound[trim_ms:trim_ms+chunk_size].dBFS < silence_threshold:
        trim_ms += chunk_size

    return trim_ms


while 1:
        record_to_file('demo.wav')
        sound = AudioSegment.from_file("demo.wav", format="wav")
        start_trim = detect_leading_silence(sound)
        end_trim = detect_leading_silence(sound.reverse())
        duration = len(sound)    
        trimmed_sound = sound[start_trim:duration-end_trim]
        #music = pyglet.resource.media('demo.wav')
        r_cmd=str(listen('demo.wav'))
        print r_cmd




