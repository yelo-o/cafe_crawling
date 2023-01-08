import requests
import urllib
import urllib2
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
from credentials import u_id, u_pw


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

url = "https://cafe.naver.com/ak573/751180"
browser.get(url)

#Requests
res = requests.get(url)
res.status_code

# 리스트 번호 불러오기
soup = bs(browser.page_source, 'html.parser')
# list = soup.find_all('div', attrs={'class':'content CafeViewer'})
# list = soup.find('div', class_ ='content CafeViewer')
rows = soup.find_all("iframe", attrs={"id" :"cafe_main"}).find("div", attrs = {"class" : "se-main-container"})

iframe = soup.find("iframe", attrs={"id" :"cafe_main"})
iframe = soup.find("iframe", attrs={"id" :"cafe_main"}).select_one('#document').attrs['src']
iframe_src = soup.select_one('#document')
src = rows['src']
response = requests.get(src)
soup_src = bs(response.text, 'html.parser')
dd = soup_src.find('span')
print(dd(['href']))

print(rows)
rows = soup.find("div", attrs={"class" : "se-module se-module-text"})
rows = soup.find("div", attrs={"class" : "se-module se-module-text"}).find_all("p")
iframexx = soup.find('iframe').find_all('')
for iframe in iframexx:
    response = urllib.requests.urlopen(iframe.attrs['src'])
    iframe_soup = bs(response)
print(rows)

iframe_html = browser.execute_script('return document.getElementsByTagName("iframe")[7]')
iframe_html2 = browser.execute_script('return iframe_html.contentWindow.document')

print(iframe_html)
print(iframe_html2)

with open('index.html', 'w') as f:
    f.write(iframe_html)

for element in iframe_html:
    print(element.text)

data = {
    "key":"value"
    }
r = requests.post(url, json=data)

print(list)