import gtts as gTTS                                       ###############################################################################
import os                                                 ###############################################################################
import os                                                 ###############################################################################
from time import sleep                                    ##########################I don't know why the hell should I###################
import requests                                           ##########################Import some modules twice. If I remove###############
from math import floor                                    ##########################the duplicates, I am getting errors...###############
from datetime import datetime                             ###############################################################################
from gtts import gTTS                                     ###############################################################################

def speaker(variable_text):
    tts = gTTS(variable_text)
    tts.save('/Applications/jarpy/audio.mp3')  
    os.system('afplay /Applications/jarpy/audio.mp3')
