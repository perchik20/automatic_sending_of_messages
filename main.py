from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


class Instagram():

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def close_all_tabs(self):
        browse = self.browser
        browse.quit()

    def login(self):

        browser = self.browser
        browser.get('https://www.instagram.com')

        time.sleep(10)

        input_name = browser.find_element(By.NAME, 'username')
        input_name.clear()
        input_name.send_keys(username)

        time.sleep(5)

        input_name = browser.find_element(By.NAME, 'password')
        input_name.clear()
        input_name.send_keys(password)

        time.sleep(5)

        input_name.send_keys(Keys.ENTER)
        print('Correct Login')
        time.sleep(20)


    def direct(self):
        browser = self.browser

        time.sleep(10)
        print('Correct Direct')
        msg_button = '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[5]/div/a'
        browser.find_element(By.XPATH, msg_button).click()

        time.sleep(15)

        msg_button = '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]'
        browser.find_element(By.XPATH, msg_button).click()

        time.sleep(15)



    def send_direct_message(self, usernames, message):
        browser = self.browser

        time.sleep(10)

        send_msg_button = '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div/div[3]/div/button'
        browser.find_element(By.XPATH, send_msg_button).click()

        time.sleep(20)

        input_username_name = 'queryBox'

        for user in usernames:
            input_user = browser.find_element(By.NAME, input_username_name)
            input_user.send_keys(user)

            time.sleep(15)

            choose_user = '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[2]/div[1]'
            browser.find_element(By.XPATH, choose_user).click()

            time.sleep(15)

        next_bth = '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[3]/div'
        browser.find_element(By.XPATH, next_bth).click()

        time.sleep(10)

        textarea_xpath = '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea'
        textarea = browser.find_element(By.XPATH, textarea_xpath)
        textarea.send_keys(message)
        textarea.send_keys(Keys.ENTER)

        time.sleep(15)

        send_button_xpath = '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/div'
        send_button = browser.find_element(By.XPATH, send_button_xpath).click()



if __name__ == '__main__':
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    usernames = input('Enter username use space between names: ').split()
    message = input('Enter the message to send: ')

    Insta = Instagram(username, password)
    Insta.login()
    Insta.direct()
    Insta.send_direct_message(usernames, message)
    Insta.close_all_tabs()
