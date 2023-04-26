import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyperclip
from credentials import u_id, u_pw


# 검색 키워드
urls = []
keywords = ['선물', '기념품']

# 셀레니움 실행
# global browser
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])  # 쓸모없는 로그 삭제
browser = webdriver.Chrome(options=options)
browser.maximize_window() # 윈도우 최대로 확대
url = "https://cafe.naver.com/ak573/"  # 인사쟁이카페 url
browser.get(url)  # 인사쟁이 카페 url로 이동

# 로그인 프로세스
## 로그인 화면 이동
btnToLogin = browser.find_element(By.XPATH,'//*[@id="gnb_login_button"]')
btnToLogin.click()

## 아이디, 비밀번호 입력
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

for keyword in keywords:
    srh = browser.find_element(By.XPATH,'//*[@id="topLayerQueryInput"]') # 검색창
    srh.send_keys(keyword)
    btn_srh = browser.find_element(By.XPATH,'//*[@id="cafe-search"]/form/button')
    btn_srh.click()
    
     # iframe 진입하기
    browser.switch_to.frame('cafe_main')
    
    # 게시글 50개씩 보이게 하기
    # browser.find_element(By.CSS_SELECTOR,"#listSizeSelectDiv").click()
    # browser.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div/div[3]/ul/li[7]/a").click()
    
    # 리스트 화면에 있는 글번호 담기
    global numList, title_list
    numList = [i.text for i in browser.find_elements(By.CSS_SELECTOR,'.inner_number')]
    
    url = 'https://cafe.naver.com/ak573/'
    for num in numList:
        urls.append(url+num)
        
     # iframe 복귀하기
    browser.switch_to.default_content()
    
    time.sleep(3)
    # browser.quit() # 브라우저 종료
print(urls, len(urls))   