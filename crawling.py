# 크롤링 관련 모듈
import requests
import urllib
import time
from datetime import datetime, timedelta
from datetime import date
from dateutil.relativedelta import relativedelta
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyperclip
import pyautogui as pg
from bs4 import BeautifulSoup as bs
import pandas as pd
from credentials import u_id, u_pw

def collect_data():
    global content_data, time_data, title_data
    browser.switch_to.frame('cafe_main')
    # 타이틀
    try:
        written_title = browser.find_elements(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[1]/div[1]/div/h3')[0]
        title_data.append(written_title.text)
    except:
        title_data.append("**접근이 불가한 게시판입니다.**")
        pass
    
    # 글 작성일자 및 시간
    try:
        written_time = browser.find_elements(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[1]/div[2]/div/div[2]/span[1]')[0]
        time_data.append(written_time.text)
    except:
        time_data.append("**접근이 불가한 게시판입니다.**")
        pass
    
    # 글 내용
    try:
        written_content = browser.find_elements(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div/div[1]')[0]
        content_data.append(written_content.text)
    except:
        content_data.append("**접근이 불가한 게시판입니다.**")
        pass
    
def moveToUrl():
    for url in urls:
        browser.get(url)
        time.sleep(1)
        collect_data()

# 메인 크롤링
def crawling_process():
    # 실행 절차
    global browser
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"]) # 쓸모없는 로그 삭제
    browser = webdriver.Chrome(options=options)
    browser.maximize_window() # 윈도우 최대로 확대
    url = "https://cafe.naver.com/ak573/"
    browser.get(url)

    # 로그인 화면 이동
    btnToLogin = browser.find_element(By.XPATH,'//*[@id="gnb_login_button"]')
    btnToLogin.click()
    today = str(date.today()) # 오늘 날짜 '2023-01-06' 과 같은 형식으로 지정
    login()
    keyword_search()
    browser.switch_to.frame('cafe_main') # iframe 진입하기

    # 게시글 50개씩 보이게 하기
    browser.find_element(By.CSS_SELECTOR,"#listSizeSelectDiv").click()
    browser.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div/div[3]/ul/li[7]/a").click()

    collect_url()
    moveToUrl()
    data_to_excel()
    browser.quit()
    
    # pg.alert(f"<{srh_krd}> 키워드로 검색한 결과 중 최근 50개의 게시글을 크롤링 완료하였습니다!")
    
def login():
    input_id = browser.find_element(By.XPATH,'//*[@id="id"]')
    input_pw = browser.find_element(By.XPATH,'//*[@id="pw"]')
    btn_lgn = browser.find_element(By.XPATH,'//*[@id="log.login"]')
    input_id.click()
    pyperclip.copy(u_id)
    input_id.send_keys(Keys.CONTROL,'v')
    input_pw.click()
    pyperclip.copy(u_pw)
    input_pw.send_keys(Keys.CONTROL,'v')
    btn_lgn.click()
    
def keyword_search():
    global srh_krd
    srh = browser.find_element(By.XPATH,'//*[@id="topLayerQueryInput"]') # 검색창
    srh_krd = '선물' # 검색 키워드 변수 저장
    srh.send_keys(srh_krd)
    btn_srh = browser.find_element(By.XPATH,'//*[@id="cafe-search"]/form/button')
    btn_srh.click()
    time.sleep(3)

def collect_url():
    # 리스트 화면에 있는 글번호 담기
    global numList, urls
    numList = [i.text for i in browser.find_elements(By.CSS_SELECTOR,'.inner_number')]
    urls = []
    url = 'https://cafe.naver.com/ak573/'
    for num in numList:
        urls.append(url+num)
        
    # 제목 담기
    global title_list
    title_list = [i.text for i in browser.find_elements(By.CSS_SELECTOR,'.article')]


# 엑셀에 데이터 저장        
def data_to_excel():
    index_list = list(range(1, len(urls)+1)) # list(range(1,51)) # 1~50까지 넘버링
    total_data = pd.DataFrame({"제목" : title_list, "날짜" : time_data, "내용" : content_data, "url" : urls}, index = index_list)
    total_data.index.name = "No."
    total_data.to_excel(f"naver cafe crawling_{crawling_time}.xlsx",index=True)

# 변수 설정
global now, st_now, crawling_time
now = datetime.now() # 시간 변수
st_now = str(now)
crawling_time = st_now[0:19].replace(':',".")
print(crawling_time)
content_data = [] # 데이터 담을 리스트
time_data = []
title_data = []