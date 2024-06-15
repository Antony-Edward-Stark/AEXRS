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
        filename = "tts.mp3"
        tts.save(filename)
        playsound3.playsound(filename)
        os.remove(filename)
    except gtts.tts.gTTSError:
        if n == 0:
            print(
                """
                .-----------------------------------------------------------------------------.
                |Can't connect to Google Text-to-Speech service, using backup server (pyttsx3)|
                '-----------------------------------------------------------------------------'
                """
            )
        

        n += 1
        engine = pyttsx3.init()
        voices = engine.getProperty("voices")
        engine.setProperty("voice", voices[0].id)
        engine.runAndWait()
        pyttsx3.speak(variable_text)
