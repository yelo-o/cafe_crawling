import pandas as pd

# 이전 크롤링 데이터 불러오기
df_old = pd.read_excel('gamdong.xlsx')

# 새로운 크롤링 데이터 불러오기
df_new = pd.read_excel('result.xlsx')

# 'F'열의 값이 겹치지 않는 데이터만 추출
df_diff = pd.concat([df_old, df_new]).drop_duplicates(subset=['url'], 
                                                      keep=False)

# 결과를 엑셀 파일로 저장
df_diff.to_excel('diff_data.xlsx', index=False)