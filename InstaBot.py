# selenium, time, sys 임포트

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import sys
import re

###########################
# chrome driver 연결 및 instagram 로그인 접속 후 해시태그 검색

driver = webdriver.Chrome("C:/Users/lsj40/Desktop/InstagramBot-main/chromedriver.exe")
driver.implicitly_wait(200)
driver.get("https://www.instagram.com/") # 인스타그램 접속

username_box_check = WebDriverWait(driver, 10).until(EC.presence_of_element_located\
((By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')))
###
driver.find_elements_by_xpath('//*[@id="loginForm"]/div/div[5]/button')[0].click() # 페이스북 로그인

username_box = driver.find_elements_by_xpath('//*[@id="email"]')[0]
username_box.send_keys("01037038419") #페이스북 ID

username_box = driver.find_elements_by_xpath('//*[@id="pass"]')[0]
username_box.send_keys("dltjdwn123!") #페이스북 PW

login_button = driver.find_elements_by_xpath('//*[@id="loginbutton"]')[0]
login_button.click() # 로그인 버튼

username_box_check = WebDriverWait(driver, 10).until(EC.presence_of_element_located\
((By.XPATH, '//section/nav/div[2]/div/div/div[2]/input')))

test = driver.find_elements_by_xpath('//div[4]/div/div/div/div[3]/button[2]')[0]
if test:    # update 뜨는 팝업 창 -> 다음에 하기 버튼 클릭
    test.click()

search_hashtag = driver.find_elements_by_xpath('//section/nav/div[2]/div/div/div[2]/input')[0]
search_hashtag.send_keys("#방탄소년단") # 해쉬태그 검색



time.sleep(3)
search_hashtag.send_keys(Keys.ENTER)
time.sleep(1)
search_hashtag.send_keys(Keys.ENTER) # 해쉬태그 검색 결과창으로 이동

current_url = driver.current_url


################
# 좋아요, 댓글 팔로우 기능


num = 0

count = 0
count_ = 0
one = 1
finish_like = False


bool_following = True

class Calculator(object): # 전역변수 이용하여 '다음' 버튼 클릭 수 누적
    def add_one(self):
        global num
        num += 1


def isHangul(text): # 한글 구별 위한 함수
    #Check the Python Version
    pyVer3 =  sys.version_info >= (3, 0)

    if pyVer3 : # for Ver 3 or later
        encText = text
    # else: # for Ver 2.x
    #     if type(text) is not unicode:
    #         encText = text.decode('utf-8')
    #     else:
    #         encText = text

    hanCount = len(re.findall(u'[\u3130-\u318F\uAC00-\uD7A3]+', encText))
    return hanCount > 0


def follow(): # 팔로우 함수

    # 새로고침같은 첫 페이지로 이동 구현하기
    global one
    global finish_like
    global count
    global count_

    A = Calculator()

    time.sleep(2)
    if finish_like == False:
        first_post = driver.find_elements_by_xpath('//div[1]/div/div/div[1]/div[1]/a')[0]
        first_post.click()
        finish_like = True
    list_ = []

    button_list = driver.find_elements_by_xpath("//button")

    for i in button_list: # 닉네임인지 확인 팔로우 부분
        list_.append(i.text)

        for j in range(len(list_)):
            
            if list_[j] == '팔로잉':
                print(list_[j])
                bool_following = True
                break
            else:
                bool_following = False


    time.sleep(2)

    if bool_following == True:
        element_list = driver.find_elements_by_xpath("//a") # a태그 찾음 다음 부분
        for j in element_list:
            if j.text == '다음':
                A.add_one()
                # Global_var.num += 1

                j.click()
                break


    elif bool_following == False:

        follow = driver.find_elements_by_xpath('//div[2]/div[1]/div[1]/span/a')[0]
        follow.click()

        # 팔로우 부분
        button_list = driver.find_elements_by_xpath("//button") # button 태그 찾음
        for i in button_list: # 닉네임인지 확인
            if i.text == '팔로우':
                follow_button = driver.find_elements_by_xpath('//div/span/span[1]/button')[0]
                follow_button.click()
                finish_like = False
                break
        
        print(num)
        # driver.get(current_url)
        for _ in range(num + 2):
            driver.back()
        
        

def like_comment(): # 좋아요 & 댓글 함수

    global count
    global one
    global finish_like

    print(count)
    if count == 3:
        
        one = 1
        follow()

    if finish_like == False and count != 3:
        if one == 1:
            first_post = driver.find_elements_by_xpath('//div[1]/div/div/div[1]/div[1]/a')[0]
            first_post.click()
            one = 2
        time.sleep(1)
        first_post_like = driver.find_elements_by_xpath('//div[3]/section[1]/span[1]/button')[0]
        first_post_like.click()
        time.sleep(1)
        
        element_list = driver.find_elements_by_xpath("//a") # 다음 click
        for j in element_list:
            if j.text == '다음':
                count += 1

                j.click()
                break
            
        if count == 3:
            exit_button = driver.find_elements_by_xpath("//div[5]/div[3]/button")[0]
            exit_button.click() 

while True:

    like_comment()

