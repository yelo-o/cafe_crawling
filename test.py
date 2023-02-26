from datetime import datetime, timedelta
import pandas as pd

'''
now = datetime.now()
print(now, type(now))
st_now = str(now)
print(st_now, type(st_now))
crawling_time = st_now[0:16].replace('-',".")  # 예) 2023-02-26 21:14
print(crawling_time)

cafe_time = ["2023.02.24. 15:49", "2023.02.24. 08:00"]
print(cafe_time)
df = pd.DataFrame({"시간" : cafe_time})
print(df)
'''

# 이전 크롤링 데이터 불러오기
df_old = pd.read_excel('gamdong.xlsx')

# 새로운 크롤링 데이터 불러오기
df_new = pd.read_excel('new_data.xlsx')

# 중복 데이터 확인
df_dup = df_new[df_new.duplicated()]

# 중복 데이터 삭제
df_new.drop_duplicates(inplace=True)

# 이전 데이터와 새로운 데이터를 합침
df_concat = pd.concat([df_old, df_new], axis=0)

# 중복 데이터 제거
df_concat.drop_duplicates(subset=['url'],keep='first', inplace=True)

# 중복 제거된 데이터를 엑셀 파일로 저장
df_concat.to_excel('result.xlsx', index=False)