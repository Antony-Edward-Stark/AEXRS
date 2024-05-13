from Foundation import *
from AppKit import NSSpeechSynthesizer
from PyObjCTools import AppHelper

def TextToSpeech():
    def __init__(self):
        self._speech_synth = NSSpeechSynthesizer.alloc().initWithVoice_(None)
        self._speech_synth.setDelegate_(self)

    def speak(self, text):
        self._speech_synth.startSpeakingString_(text)
        AppHelper.runConsoleEventLoop()  # Wait for speech to finish

    def stop(self):
        self._speech_synth.stopSpeaking()

tts = TextToSpeech()
tts.speak("Hello, world! This is spoken text using macOS's built-in synthesizer.")
tts.stop()
