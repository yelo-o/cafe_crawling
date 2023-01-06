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
    u_id = pg.prompt(text="아이디를 입력하세요.", title = '아이디')
    u_pw = pg.password(text="비밀번호를 입력하세요.", title = '비밀번호', mask="*")
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
url = "https://cafe.naver.com/ak573"
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

# 게시글 50개씩 보이게 하기
# browser.find_element_by_css_selector("#listSizeSelectDiv").click()
browser.find_element(By.CSS_SELECTOR,"#listSizeSelectDiv").click()
# browser.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div[3]/ul/li[7]/a").click()
browser.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div/div[3]/ul/li[7]/a").click()

# 제목
today = str(date.today()) # 오늘 날짜 '2023-01-06' 과 같은 형식으로 지정

title = [i.text for i in browser.find_elements(By.CSS_SELECTOR,'.article')]
numList = [i.text for i in browser.find_elements(By.CSS_SELECTOR,'.inner_number')]
# author = [i.text for i in browser.find_elements(By.CSS_SELECTOR,'.m-tcol-c')]
writtenDate = [i.text for i in browser.find_elements(By.CSS_SELECTOR,'.td_date')]
# print(title)
# print(numList)
# print(writtenDate)

# 판다스 데이터 밀어넣기
total_data = pd.DataFrame()
total_data['순번'] = pd.Series(numList)
total_data['제목'] = pd.Series(title)
# total_data['작성자'] = pd.Series(author)
total_data['날짜'] = pd.Series(writtenDate)
print(total_data)
total_data.to_excel(f"인사쟁이카페 데이터 크롤링{today}.xlsx",index=True)

# titleList = browser.find_elements(By.CLASS_NAME,'article')
# for j in titleList:
#     a = j.get_attribute(j.text)
#     print(f"타이틀: {j}", a)

# # 스크롤링할 데이터 담을 리스트 설정
# list_title = []
# list_author = []
# list_time = []
# list_content = []
# title = 
# content = browser.find_element(By.XPATH,'//*[@id="SE-6e2c1f9f-2b03-478c-b6cb-4e5e30d007fa"]/div/div/div')



# # 변수 설정
# save_path = "./"
# count = 0
# sData = [] # DataFrame 전환리스트 
# nTitle = [] # 게시글 제목
# nNickname = [] # 카페 닉네임
# nUrl = [] # 게시글 링크
# nContent = [] # 게시글 내용
# nIDs = [] # 게시글 사용자 정보

# # 검색

# # 날짜 지정
# today = str(date.today()) # 오늘 날짜 '2023-01-06' 과 같은 형식으로 지정
# now = datetime.now()
# before_1day = now - timedelta(days=1, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
# print(before_1day.now)
# before_2day = now - timedelta(days=2, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
# before_2day.now()
# before_3day = now - timedelta(days=3, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
# selected_days = []


# # 
# for page in tqdm(range(1,11)):
    