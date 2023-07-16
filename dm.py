from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login import Login
import time


log = Login()
driver = log.login()

time.sleep(5)

name = str(input("ENTER THE USERNAME FOR DMS :"))
text = "checking it is working or not!!"

username = name
time.sleep(10)
driver.get("https://www.instagram.com/direct/inbox/")
time.sleep(3)

wait = WebDriverWait(driver, 10)

notification_popup = wait.until(EC.visibility_of_element_located((By.XPATH, '//div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')))
if notification_popup.is_displayed():
    notification_popup.click()
    time.sleep(2)


message1 = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div[4]/div')))
message1.click()
time.sleep(2)

search1 = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/input')))
search1.click()

time.sleep(2)

search1 = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/input')))
search1.clear()
search1 = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/input')))
search1.send_keys(username)

search1 = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/input')))
search1.send_keys(Keys.RETURN)

time.sleep(1)

click1 = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[3]/div/div/div/div[1]/div/div/div[2]/div/div')))
click1.click()

time.sleep(2)

chat1 = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[4]/div')))
chat1.click()

time.sleep(2)

send_msg1 = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]/p')))
send_msg1.click()

time.sleep(2)

send_msg1 = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]/p')))
send_msg1.clear()
send_msg1.send_keys(text)

time.sleep(2)

send_msg1 = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]/p')))
send_msg1.send_keys(Keys.RETURN)

time.sleep(10)
driver.close()
