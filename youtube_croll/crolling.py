from bs4 import BeautifulSoup
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
# 드라이버 bluetooth 자동종료 제거 option
driver = webdriver.Chrome("./chromedriver89.exe", options = options)
driver.implicitly_wait(200)


def youtube_croll(url):

    driver.get(url)
    # driver 통해 받아온 소스 html 변수에 저장
    html = driver.page_source
    # bs통해 parse
    soup = BeautifulSoup(html, 'html.parser')

    # 가수 뽑아오는 태그
    songs = soup.select('#video-title')  
    # 등록자 뽑아오는 태그
    author = soup.select('div > #byline')  

    for i in range(len(songs)):
        print(str(i + 1) + "위: 제목-> " + songs[i].getText().strip())
        print("      가수-> " + author[i].getText())

# youtube url
url = 'https://www.youtube.com/watch?v=waRLFDHPGew&list=PL4fGSI1pDJn6jXS_Tv_N9B8Z0HTRVJE0m&index=1'
youtube_croll(url)
