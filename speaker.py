import gtts.tts
from gtts import gTTS
import pyttsx3
import playsound3
import os

n = 0


def speaker(variable_text):
    global n
    try:
        tts = gTTS(variable_text, lang="en")
        filename = ".\\aud.mp3"
        tts.save(filename)
        playsound3.playsound(filename)
        os.remove(filename)

    except gtts.tts.gTTSError:
        n += 1
        class _TTS:
            engine = None
            rate = None
            def __init__(self):
                self.engine = pyttsx3.init()
            def start(self,text_):
                self.engine.say(text_)
                self.engine.runAndWait()
        tts = _TTS()
        tts.start(variable_text)
        del(tts)
