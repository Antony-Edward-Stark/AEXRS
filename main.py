import re
import os
import speech_recognition as recognition
import pyttsx3

recogniser = recognition.Recognizer()
os.system('cls')

#to speak the text produced...
def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text) 
    engine.runAndWait()

for i in range(2):    
    try:
        # use the microphone as source for input.
        with recognition.Microphone() as source2:
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level 
            recogniser.adjust_for_ambient_noise(source2, duration=0.2)
            print("Speak Anything :")
            #listens for the user's input 
            audio2 = recogniser.listen(source2)
            # Using google to recognize audio
            MyText = recogniser.recognize_google(audio2)
            MyText = MyText.lower()
            print("Did you say ",MyText)
            speak_text(MyText)
    except recognition.RequestError as e:
        print("Could not request results; {0}".format(e))
    except recognition.UnknownValueError as e:
        print("unknown error occurred")
        print(e)
