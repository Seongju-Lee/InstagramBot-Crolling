# selenium 임포트

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import sys
import re


# chrome driver 연결 및 instagram 로그인 접속 후 해시태그 검색

driver = webdriver.Chrome("C:/Users/lsj40/Documents/GitHub/InstagramBot/chromedriver/chromedriver88.exe")
driver.implicitly_wait(200)
driver.get("https://www.instagram.com/") # 인스타그램 접속

username_box_check = WebDriverWait(driver, 10).until(EC.presence_of_element_located\
((By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')))
################## facebook 버전 로그인
# driver.find_elements_by_xpath('//*[@id="loginForm"]/div/div[5]/button')[0].click() # 페이스북 로그인

# username_box = driver.find_elements_by_xpath('//*[@id="email"]')[0]
# username_box.send_keys("ID") #페이스북 ID

# username_box = driver.find_elements_by_xpath('//*[@id="pass"]')[0]
# username_box.send_keys("PW") #페이스북 PW

# login_button = driver.find_elements_by_xpath('//*[@id="loginbutton"]')[0]
# login_button.click() # 로그인 버튼
###############


######### 인스타 전용 계정 로그인

username_box = driver.find_elements_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')[0]
username_box.send_keys("ID")

username_box = driver.find_elements_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')[0]
username_box.send_keys("PW")

login_button = driver.find_elements_by_xpath('//*[@id="loginForm"]/div/div[3]/button')[0]
login_button.click() # 로그인 버튼



username_box_check = WebDriverWait(driver, 10).until(EC.presence_of_element_located\
((By.XPATH, '//section/nav/div[2]/div/div/div[2]/input')))

test = driver.find_elements_by_xpath('//div[4]/div/div/div/div[3]/button[2]')[0]
if test:    # update 뜨는 팝업 창 -> 다음에 하기 버튼 클릭
    test.click()

search_hashtag = driver.find_elements_by_xpath('//section/nav/div[2]/div/div/div[2]/input')[0]
search_hashtag.send_keys("#코딩") # 해쉬태그 검색


time.sleep(3)
search_hashtag.send_keys(Keys.ENTER)
time.sleep(1)
search_hashtag.send_keys(Keys.ENTER) # 해쉬태그 검색 결과창으로 이동

current_url = driver.current_url


# 좋아요, 댓글 팔로우 기능

count = 0
count_ = 0
one = 1
finish_like = False

bool_ = True
bool_following = True

def isHangul(text): # 한글 구별 위한 함수
    #Check the Python Version
    pyVer3 =  sys.version_info >= (3, 0)

    if pyVer3 : # for Ver 3 or later
        encText = text
    

    hanCount = len(re.findall(u'[\u3130-\u318F\uAC00-\uD7A3]+', encText))
    return hanCount > 0


def like_comment(): # 좋아요 & 댓글 함수

    global count
    global one
    global finish_like

    print(count)
    if count == 30:
        
        one = 1
        sys.exit('설정한 횟수가 끝났습니다.')
        # 또는 팔로우 목록으로 이동하여 팔로워와 팔로우 차이 많이 나는 팔로워 제거하기..

    ################################# 첫번째 게시물 선택
    if finish_like == False and count != 30:
        if one == 1:
            first_post = driver.find_elements_by_xpath('//div[1]/div/div/div[1]/div[1]/a')[0]
            first_post.click()
            one = 2

    ################################
        time.sleep(5)
        
        ############################## 좋아요            
        like_action = driver.find_elements_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button')[0]

        like_path = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button/div/span/*[name()="svg"]')
        like_text = like_path.get_attribute('aria-label')
        if like_text == "좋아요":
            print("좋아요 클릭")
            like_action.click()
        else:
            print("이미 좋아요")

        #############################
        time.sleep(5)

        ################################# 팔로우

        list_ = []

        button_list = driver.find_elements_by_xpath("//button")

        for i in button_list:
            list_.append(i.text)
        time.sleep(2)

        if list_[1] == '팔로잉':
            bool_following = True
            pass
        else:
            bool_following = False
            follow_btn = driver.find_elements_by_xpath('//div[2]/div[1]/div[2]/button')[0]
            follow_btn.click()
        #######################################
        time.sleep(6)

        ###################################### 다음 게시물로 이동
        element_list = driver.find_elements_by_xpath("//a") # 다음 click
        for j in element_list:
            if j.text == '다음':
                count += 1
                bool_ = False
                j.click()
                break
            
        if count == 30:
            exit_button = driver.find_elements_by_xpath("//div[5]/div[3]/button")[0]
            exit_button.click() 
        #####################################

while True:

    like_comment()

