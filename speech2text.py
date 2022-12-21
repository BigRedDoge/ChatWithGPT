import speech_recognition as sr


class Speech2Text:

    def __init__(self):
        self.r = sr.Recognizer()

    def listen(self):
        with sr.Microphone() as source:
            audio = self.r.listen(source)
        try:
            text = self.r.recognize_google(audio)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return text


if __name__ == '__main__':
    stt = Speech2Text()
    print(stt.listen())