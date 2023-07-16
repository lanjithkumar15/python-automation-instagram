from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login import Login
import time


log = Login()
driver = log.login()
   
time.sleep(10)

name = str(input("ENTER THE USERNAME FOR LIKE :"))
username = name
driver.get("https://www.instagram.com/" + username)

wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, '_aagw')))
element.click()

time.sleep(3)

wait = WebDriverWait(driver, 10)
like1 = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/div/div')))
like1.click()

wait = WebDriverWait(driver, 10)
next1 = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div/button')))
next1.click()

time.sleep(2)


wait = WebDriverWait(driver, 10)
like2 = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/div')))
like2.click()
time.sleep(2)

wait = WebDriverWait(driver, 10)
next2 = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button')))
next2.click()
time.sleep(3)

wait = WebDriverWait(driver, 10)
like3 = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/div')))
like3.click()
time.sleep(2)

time.sleep(10)
driver.quit()
