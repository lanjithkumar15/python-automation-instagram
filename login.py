import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Login:
    def login(self):
        username = 'dummy00890'
        password = 'dummy008901'

        driver = webdriver.Chrome()


        driver.get('https://www.instagram.com/accounts/login/')

        login_form = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, 'form'))
        )


        username_input = driver.find_element(By.NAME, 'username')
        username_input.send_keys(username)


        password_input = driver.find_element(By.NAME, 'password')
        password_input.send_keys(password)


        login_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        login_button.click()

        return driver
