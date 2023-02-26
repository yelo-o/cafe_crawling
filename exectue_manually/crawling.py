# 크롤링 관련 모듈
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyperclip
import pyautogui as pg
from bs4 import BeautifulSoup as bs
import pandas as pd
from credentials import u_id, u_pw

# 변수 설정
now = datetime.now()
st_now = str(now)
crawling_time = st_now[0:19].replace(':',".")
print(crawling_time)
# 엑셀 열 구성 데이터
time_data = [] # 날짜 + 시간 열
date_column = [] # 날짜 열
time_column = [] # 시간 열
title_data = [] # 제목 열
content_data = [] # 내용 열

# 메인 프로세스(최초 로그인)
def crawling_process(srh_krd):
    global now, st_now, crawling_time, time_data, time_column, date_column, title_data, content_data
    execute_browser() # 브라우저 실행 및 url 이동
    login() # 로그인 화면 이동 및 로그인
    keyword_search(srh_krd) # '선물' 키워드 검색
    collect_url() # '화면에 표시되는 50개의 url 수집'
    moveToUrl() # 수집한 url로 이동
    data_to_excel(crawling_time, srh_krd)  # 데이터 엑셀로 변환
    browser.quit() # 브라우저 종료
    
    # 리스트 데이터들을 한번 초기화 시켜줘야 함
    time_data = []
    time_column = []
    date_column = []
    time_data = []
    content_data= []

    # pg.alert(f"<{srh_krd}> 키워드로 검색한 결과 중 최근 50개의 게시글을 크롤링 완료하였습니다!")

# 메인 프로세스2 (키워드 두번째 검색)
# def crawling_process_second_keyword(srh_krd):
#     browser.switch_to.default_content()
#     global now, st_now, crawling_time, time_data, time_column, date_column, title_data, content_data
#     keyword_search(srh_krd) # '선물' 키워드 검색
#     collect_url() # '화면에 표시되는 50개의 url 수집'
#     moveToUrl() # 수집한 url로 이동
#     data_to_excel(crawling_time, srh_krd)  # 데이터 엑셀로 변환
#     browser.quit() # 브라우저 종료
    
# 브라우저 실행 및 url 이동
def execute_browser():
    global browser
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"]) # 쓸모없는 로그 삭제
    browser = webdriver.Chrome(options=options)
    browser.maximize_window() # 윈도우 최대로 확대
    url = "https://cafe.naver.com/ak573/"
    browser.get(url)
def login():
    # 로그인 화면 이동
    btnToLogin = browser.find_element(By.XPATH,'//*[@id="gnb_login_button"]')
    btnToLogin.click()

    # 아이디, 비밀번호 입력
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
# 선물/기념품 키워드 검색
def keyword_search(srh_krd):
    srh = browser.find_element(By.XPATH,'//*[@id="topLayerQueryInput"]') # 검색창
    srh.send_keys(srh_krd)
    btn_srh = browser.find_element(By.XPATH,'//*[@id="cafe-search"]/form/button')
    btn_srh.click()
def collect_url():
    # iframe 진입하기
    browser.switch_to.frame('cafe_main')
    
    # 게시글 50개씩 보이게 하기
    # browser.find_element(By.CSS_SELECTOR,"#listSizeSelectDiv").click()
    # browser.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div/div[3]/ul/li[7]/a").click()
    
    # 리스트 화면에 있는 글번호 담기
    global numList, urls, title_list
    numList = [i.text for i in browser.find_elements(By.CSS_SELECTOR,'.inner_number')]
    urls = []
    url = 'https://cafe.naver.com/ak573/'
    for num in numList:
        urls.append(url+num)
    # 제목 담기
    title_list = [i.text for i in browser.find_elements(By.CSS_SELECTOR,'.article')]
    time.sleep(3)

# 수집한 url로 이동
def moveToUrl():
    for url in urls:
        browser.get(url)
        # time.sleep(1)
        browser.implicitly_wait(1)
        collect_data()

# 제목, 내용, 작성시간 수집
def collect_data():
    global content_data, time_data, title_data, date_column, time_column
    # 데이터 담을 리스트 생성

    browser.switch_to.frame('cafe_main')
    # 타이틀 -> title_data
    try:
        written_title = browser.find_elements(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[1]/div[1]/div/h3')[0]
        title_data.append(written_title.text)
    except:
        title_data.append("**접근이 불가한 게시판입니다.**")
        pass
    # 글 작성일자 및 시간 -> time_data
    try:
        written_time = browser.find_elements(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[1]/div[2]/div/div[2]/span[1]')[0]
        time_data.append(written_time.text)
    except:
        time_data.append("**접근이 불가한 게시판입니다.**")
        pass
    # 글 내용 -> content_data
    try:
        written_content = browser.find_elements(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div/div[1]')[0]
        content_data.append(written_content.text)
    except:
        content_data.append("**접근이 불가한 게시판입니다.**")
        pass

# 엑셀에 데이터 저장
def data_to_excel(crawling_time, srh_krd):
    # 시간 열 나누기 (1개 -> 2개)
    global time_data
    for time in time_data:
        global date_column, time_column
        a = time.split()
        date_column.append((a[0]))
        time_column.append((a[1]))
    # 판다스 데이터 프레임 만들기
    index_list = list(range(1, len(urls)+1)) # list(range(1,51)) # 1~50까지 넘버링
    total_data = pd.DataFrame({"제목" : title_list, "날짜" : date_column, "시간" : time_column, "내용" : content_data, "url" : urls}, index = index_list)
    total_data.index.name = "No."
    total_data.to_excel(f"{crawling_time}-{srh_krd}검색.xlsx",index=True)

# 감동타임 키워드
crawling_process(srh_krd='선물')
crawling_process(srh_krd='기념품')
