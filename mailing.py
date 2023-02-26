# 메일 관련 모듈
import sys, os
import smtplib
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.encoders import encode_base64

# 외부 변수
from exectue_manually.crawling import crawling_time

# 메일보내기 함수
def mailing():
    smtp_etners = smtplib.SMTP('mail.etners.com', 25)
    smtp_etners.ehlo()
    msg = MIMEMultipart()

    # 제목 입력
    # msg['subject'] = f'[{crawling_time}]네이버 카페 크롤링 공유의 件'
    msg['subject'] = f'[인사쟁이 카페 크롤링] {crawling_time} 件'
    # 보내는 사람
    msg['From'] = '김민규 <flyordig@etners.com>'
    # 받는 사람
    # msg['To'] = ", ".join(['hjs0131@etners.com', 'orion@etners.com']) # 수신자가 다수일 때
    # msg['To'] = 'hjs0131@etners.com' # 한진솔 프로
    msg['To'] = 'flyordig@etners.com' # 테스트용(본인 계정)
    # 참조
    # msg['Cc'] = ", ".join(['orion@etners.com', 'flyordig@etners.com'])
    # 내용 입력
    body = MIMEText(f" 안녕하세요,\n\n 경영혁신그룹 크롤링 봇입니다. \n\n {crawling_time} 에 [인사쟁이 카페]에서 '선물' 키워드로 크롤링 진행한 엑셀 파일 전달드립니다.\n\n감사합니다.", _charset = 'utf-8')
    msg.attach(body)

    # 첨부 파일
    path = f'C:/Users/user/Desktop/VENVWorkspace/cafe_crawling/naver cafe crawling_{crawling_time}.xlsx'
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(open(path, "rb").read())
    encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(path))
    msg.attach(part)

    # 메일 송신
    smtp_etners.send_message(msg)