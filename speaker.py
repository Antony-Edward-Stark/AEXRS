from gtts import gTTS                                    
import os                                               

def speaker(variable_text):
    tts = gTTS(variable_text)
    tts.save('/Applications/jarpy/audio.mp3')  
    os.system('afplay /Applications/jarpy/audio.mp3')
