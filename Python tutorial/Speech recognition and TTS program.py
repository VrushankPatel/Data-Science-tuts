import subprocess
import speech_recognition as sr
import pyglet
from gtts import gTTS


def get():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak anything : ")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            print("You said {}", format(text))
            return str(text)
        except:
            print("Sorry, couldn't recognise your voice")
            return "Sorry, couldn't recognise your voice"


speech = gTTS(text=get(), lang='hi', slow=False)
speech.save("test.mp3")
return_code = subprocess.call(["afplay", "test.mp3"])
