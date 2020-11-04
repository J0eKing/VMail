import speech_recognition as sr
import winsound
import pyttsx3 as p
import webview

def say(thing):
    e = p.init()
    e.say(thing)
    e.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Talk")
        winsound.Beep(440, 250)
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(text)

            return text
        except:
            return "@#"
