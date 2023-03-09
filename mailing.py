# 메일 관련 모듈
import sys, os
import smtplib
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.encoders import encode_base64
import pandas as pd
import openpyxl


# 외부 변수
from cr import crawling_time
# file_name = 'diff_data.xlsx'
file_name = f'{crawling_time} 감동타임 키워드 신규 검색 결과.xlsx'

# Only New Data
df_diff = pd.read_excel(f'{crawling_time} 감동타임 키워드 신규 검색 결과.xlsx')

# 메일보내기 함수
def mailing():
    smtp_etners = smtplib.SMTP('mail.etners.com', 25)
    smtp_etners.ehlo()
    msg = MIMEMultipart()
    msg.set_charset("utf-8")

    # 제목 입력
    # msg['subject'] = f'[{crawling_time}]네이버 카페 크롤링 공유의 件'
    msg['subject'] = f'[감동타임] 인사쟁이카페 크롤링 데이터 공유의 件_ {crawling_time} '
    # 보내는 사람
    msg['From'] = '김민규 <flyordig@etners.com>'
    
    # 수신인
    # msg['To'] = ", ".join(['hjs0131@etners.com', 'orion@etners.com']) # 수신자가 다수일 때
    msg['To'] = 'nary0907@etners.com' # 김나리
    # msg['To'] = 'flyordig@etners.com' # 테스트용(본인 계정)
    
    # 참조
    msg['Cc'] = ", ".join(['cjkaszzang@etners.com', 'mijung806@etners.com',
                           'haeun1106@etners.com', 'flyordig@etners.com']) # 심대현, 권아성, 박미정, 김하은, 김민규, 한진솔
    # msg['Cc'] = ", ".join(['flyordig@etners.com','hyew7920@etners.com']) # 단체 테스트용
    
    # 내용 입력
    body = MIMEText(f" 안녕하세요,\n\n 디지털혁신그룹 크롤링 봇입니다. \n\n {crawling_time} 에 [인사쟁이 카페]에서 감동타임 키워드 크롤링 진행한 엑셀 파일 전달드립니다.\n\n*해당 데이터는 크롤링 시간 기준 신규 인입 데이터이며, \n\n 사람의 개입없이 자동발송되므로 BO여부를 사전에 판단하지 못 하는점 양해부탁드립니다.\n\n□ 현재 검색 키워드 \n\t- 선물\n\t  - 기념품 \n\n감사합니다.", _charset = 'utf-8')
    msg.attach(body)

    # 첨부 파일 (기존)
    path = f'C:/flyordig/cafe_crawling/{crawling_time} 감동타임 키워드 신규 검색 결과.xlsx'
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(open(path, "rb").read())
    encode_base64(part)
    # part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(path))
    part.add_header('Content-Disposition', 'attachment', filename=file_name)
    msg.attach(part)
    

    # 메일 송신
    smtp_etners.send_message(msg)


# 새로운 행이 생길 때만 메일 발송


# 엑셀 파일 열기
workbook = openpyxl.load_workbook(f'{crawling_time} 감동타임 키워드 신규 검색 결과.xlsx')

# 시트 선택하기
sheet = workbook.active

# 2번째 행에 데이터가 있는 경우에만 함수 실행하기
if sheet.cell(row=2, column=1).value is not None:
    mailing()
