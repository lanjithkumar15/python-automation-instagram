from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login import Login
import time

log = Login()
driver = log.login()

time.sleep(10)
name = str(input("ENTER THE USERNAAME FOR COMMENTING :"))
username = name
time.sleep(10)
driver.get("https://www.instagram.com/" + username)

time.sleep(3)

wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, '_aagw')))
element.click()

time.sleep(7) 

text = "good work it is best post!"

wait = WebDriverWait(driver, 10)
comment_input = driver.find_element(By.CSS_SELECTOR, 'textarea[aria-label="Add a comment…"]')
comment_input.click()

comment_input = driver.find_element(By.CSS_SELECTOR, 'textarea[aria-label="Add a comment…"]')
comment_input.clear()
comment_input.send_keys(text)

comment_input = driver.find_element(By.CSS_SELECTOR, 'textarea[aria-label="Add a comment…"]')
comment_input.send_keys(Keys.RETURN)

time.sleep(5)
driver.quit()
