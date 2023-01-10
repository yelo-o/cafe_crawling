import os
import smtplib
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.encoders import encode_base64

from datetime import datetime, timedelta # 시간 변수
from datetime import date

# 시간 변수 설정
now = datetime.now()
st_now = str(now)
crawling_time = st_now[0:19].replace(':',".")
print(crawling_time) # 크롤링 시간 확인

def mailing():
    smtp_etners = smtplib.SMTP('mail.etners.com', 25)
    smtp_etners.ehlo()
    msg = MIMEMultipart()

    # 제목 입력
    msg['subject'] = f'[{crawling_time}]네이버 카페 크롤링 공유의 件'
    # 보내는 사람
    msg['From'] = 'et_innov@etners.com'
    # 받는 사람
    msg['To'] = 'flyordig@etners.com' 
    # 내용 입력
    body = MIMEText(f" 안녕하세요,\n 경영혁신그룹입니다. \n {crawling_time}에 [인사쟁이 카페] 크롤링 진행한 엑셀 파일 전달드립니다.", _charset = 'utf-8')
    msg.attach(body)

    # 첨부 파일
    path = f'C:/Users/user/Desktop/VENVWorkspace/cafe_crawling/dist/main/naver cafe crawling_{crawling_time}.xlsx'
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(open(path, "rb").read())
    encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(path))
    msg.attach(part)

    # 메일 송신
    smtp_etners.send_message(msg)