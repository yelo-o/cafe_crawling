import schedule
import time

def message1():
    print("스케쥴 실행 중...")

def message2(text):
    print(text)
    
def crawling_process():
    pass
# 주기 설정
# 매일 15시
schedule.every().day.at("15:00").do(crawling_process)


job1 = schedule.every(1).seconds.do(message1)
job2 = schedule.every(2).seconds.do(message2, "2초마다 알려줄게용")

count = 0

while True:
    
    schedule.run_pending()
    time.sleep(1)
    
    count = count + 1
    print(count)
    
    if count>5:
        schedule.cancel_job(job1)

    