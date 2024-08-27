import pyttsx3
variable_text = 'hello'
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