from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome("C:/Users/eunhaengdong/Desktop/pypy/chromedriver87.exe")
driver.implicitly_wait(200)
driver.get("https://www.instagram.com/")

username_box_check = WebDriverWait(driver, 10).until(EC.presence_of_element_located\
((By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')))


driver.find_elements_by_xpath('//*[@id="loginForm"]/div/div[5]/button')[0].click()

# username_box = driver.find_elements_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')[0]
# username_box.send_keys("your_id")
# password_box = driver.find_elements_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')[0]
# password_box.send_keys("your_password!")
# login_button = driver.find_elements_by_xpath('//*[@id="loginForm"]/div/div[3]/button')[0]
# login_button.click()

# xpath = "//article//section/span/button"
# print(len(driver.find_elements_by_xpath(xpath)))
