from gtts import gTTS
from playsound import playsound
import os
from datetime import datetime

class Text2Speech:

    def say(self, text):
        filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".mp3"
        tts = gTTS(text=text, lang='en')
        tts.save(filename)
        playsound(filename)
        os.remove(filename)


if __name__ == '__main__':
    tts = Text2Speech()
    tts.say('Hello World')