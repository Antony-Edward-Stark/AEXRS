import gtts as gTTS
import os
import os
from time import sleep
import requests
from math import floor
from datetime import datetime
from gtts import gTTS

def speaker(variable_text):
    tts = gTTS(variable_text)
    tts.save('/Applications/jarpy/audio.mp3')  
    os.system('afplay /Applications/jarpy/audio.mp3')