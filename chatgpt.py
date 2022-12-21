from selenium import webdriver
from selenium.webdriver.common.by import By

class ChatGPT:

    def __init__(self):
        self.driver = webdriver.Chrome()
        

    def chat(self, text):
        self.send_chat(text)
        return self.get_response()

    def send_chat(self, text):
        pass

    def get_response(self):
        pass

    def new_session(self):
        pass

    def close_session(self):
        self.driver.close()

    def start_session(self):
        self.driver.get('https://chat.openai.com/chat')
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[4]/button[1]').click()