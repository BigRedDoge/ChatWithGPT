from speechtext import SpeechText
from chatgpt import ChatGPT


def chatwithgpt(chatgpt):
    while True:
        stt = SpeechText()
        text = stt.listen()
        #print(text)
        if text == "quit":
            break
        if text == "ERROR":
            continue
        response = chatgpt.chat(text)
        #print(response)
        stt.say(response)

if __name__ == '__main__':
    chatgpt = ChatGPT()
    chatgpt.start_session()

    chatgpt.chat("I want you to act as a personal assistant. You will respond to my prompt as if you were my secretary.  Do not mention you are a language model.  Keep responses short and concise.  Please wait for my first prompt.")

    chatwithgpt(chatgpt)
    chatgpt.close_session()