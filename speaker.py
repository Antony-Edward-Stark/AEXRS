import os
from gtts import gTTS

def speaker(variable_text):
    tts = gTTS(variable_text)
    tts.save('/Applications/jarpy/audio.mp3')  
    os.system('afplay /Applications/jarpy/audio.mp3')