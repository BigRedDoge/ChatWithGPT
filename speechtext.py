import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os
from datetime import datetime

class SpeechText:

    def __init__(self):
        self.r = sr.Recognizer()

    def listen(self):
        text = ""
        with sr.Microphone() as source:
            audio = self.r.listen(source)
        try:
            text = self.r.recognize_google(audio)
        except sr.UnknownValueError:
            text = "ERROR"
        except sr.RequestError as e:
            text = "ERROR"
        return text

    def say(self, text):
        filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".mp3"
        tts = gTTS(text=text, lang='en')
        tts.save(filename)
        playsound(filename)
        os.remove(filename)

if __name__ == '__main__':
    stt = SpeechText()
    stt.say(stt.listen())