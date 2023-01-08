import requests
import time
from datetime import datetime, timedelta
from datetime import date
from dateutil.relativedelta import relativedelta
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import openpyxl
import sys, os
import pyperclip
import pyautogui as pg
from bs4 import BeautifulSoup as bs
import pandas as pd

# 로그인
"""
pyperclip 모듈을 이용해서 아이디, 비밀번호 복사 붙여넣기
    - > 일반 셀레니움으로 입력하면 네이버에서 크롤링 봇 감지하여 자동입력방지  
"""
def login():
    input_id = browser.find_element(By.XPATH,'//*[@id="id"]')
    input_pw = browser.find_element(By.XPATH,'//*[@id="pw"]')
    btn_lgn = browser.find_element(By.XPATH,'//*[@id="log.login"]')
    # u_id = pg.prompt(text="아이디를 입력하세요.", title = '아이디')
    # u_pw = pg.password(text="비밀번호를 입력하세요.", title = '비밀번호', mask="*")
    u_id = 'flyordig'
    u_pw = 'vhffkchdltm@19'
    input_id.click()
    pyperclip.copy(u_id)
    input_id.send_keys(Keys.CONTROL,'v')
    input_pw.click()
    pyperclip.copy(u_pw)
    input_pw.send_keys(Keys.CONTROL,'v')
    btn_lgn.click()

# 인사쟁이카페 진입
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"]) # 쓸모없는 로그 삭제
browser = webdriver.Chrome(options=options)
browser.maximize_window() # 윈도우 최대로 확대
url = "https://cafe.naver.com/ak573/"
browser.get(url)
# 로그인 화면 이동
btnToLogin = browser.find_element(By.XPATH,'//*[@id="gnb_login_button"]')
btnToLogin.click()
login()
# 키워드 검색
srh = browser.find_element(By.XPATH,'//*[@id="topLayerQueryInput"]') # 검색창
srh_krd = '선물' # 검색 키워드 변수 저장
srh.send_keys(srh_krd)
btn_srh = browser.find_element(By.XPATH,'//*[@id="cafe-search"]/form/button')
btn_srh.click()
time.sleep(3)

# iframe 진입
browser.switch_to.frame('cafe_main')
soup = bs(browser.page_source, 'html.parser')

# # 게시글 50개씩 보이게 하기
# browser.find_element(By.CSS_SELECTOR,"#listSizeSelectDiv").click()
# browser.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div/div[3]/ul/li[7]/a").click()

# 리스트 번호 불러오기
numList = [i.text for i in browser.find_elements(By.CSS_SELECTOR,'.inner_number')]
urls = [] # 기본 url + 리스트번호 로 파싱할 url주소들 얻기
for num in numList:
    urls.append(url+num)
# print(urls)
page = requests.get(urls[0])
soup = bs(browser.page_source, 'html.parser')
# list = soup.find_all(attrs={'class': 'content CafeViewer'})
# list = soup.select_one(attrs={'class':'se-fs- se-ff-   '})
# list = soup.find_all('span', attrs={'class':'se-fs- se-ff-   '})
# list = soup.find_all('div', attrs={'class':'se-module se-module-text'})
list = soup.select_one('div', attrs={'class':'se-module se-module-text'})
# content = soup.find('div.article_container')
print(list)
# print(content)