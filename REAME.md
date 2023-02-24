# 모듈 설치
    - pip install selenium openpyxl pyperclip python-dateutil beautifulsoup4 pandas requests pyautogui

# 함수 분리
0. main.py
    - 실행 파일
1. credentials.py
    - 네이버 아이디와 비밀번호가 있는 파일
2. crawling.py
    - 네이버카페 크롤링
3. excel_processing.py
    - 엑셀 후처리(열너비, 가운데 정렬 등..)
4. mailing.py
    - 메일링 연동


# 2023.02.24(금)
    - 2023.02.27부로 감동타임으로 이관
        . 검색해서 새로운 검색 결과 데이터가 있을 경우에만 메일 발송
