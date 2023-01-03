import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import openpyxl
import sys, os
import pyperclip
import pyautogui as pg

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
    u_pw = pg.prompt(text="비밀번호를 입력하세요.", title = '비밀번호')
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

# 검색

# 