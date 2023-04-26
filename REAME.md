## 깃 허브 다운로드 -> 모듈 설치 -> 실행 확인

## 실행되기 위한 조건
```
- 파일 확인
    · crawler.py
    · get_urls.py
    · cr.py
    · proc.py
    · mailing.py
    · credentials.py  
```
```
★ credentials.py는 보안으로 인해 깃허브에 올려놓지 않았으므로 직접 파일을 만들어 내용 입력
credentials.py를 새로 만들어서 양식에 맞게 아이디와 비밀번호 입력 양식은 아래의 함수 설명 참조
```

## 모듈 설치
```
pip install selenium openpyxl pyperclip python-dateutil beautifulsoup4 pandas requests pyautogui
# cmd(명령프롬프트)에 상기의 명령어를 입력하여 모듈 다운로드
```
## 함수 설명
### 0. crawler.py
    - 실행 파일
### 1. credentials.py 
    - 네이버 아이디와 비밀번호가 있는 파일
      · 디렉토리에 해당 이름으로 파일 생성 후, 아래의 양식과 같이 작성
```
u_id = '네이버 아이디'
u_pw = '네이버 비밀번호'
```

### 2. crawling.py
    - 네이버카페 크롤링
### 3. excel_processing.py
    - 엑셀 후처리(열너비, 가운데 정렬 등..)
### 4. mailing.py
    - 메일링 연동

## 2023.02.24(금)
    - 2023.02.27부로 감동타임으로 이관
        . 검색해서 새로운 검색 결과 데이터가 있을 경우에만 메일 발송

## 2023.02.27(월) 작업 完
```
   - "gamdong.xlsx"로 누적 데이터 관리
   - "{크롤링시간}감동타임 키워드 신규 검색 결과.xlsx" → 메일로 보낼 파일
   - 상기 이름으로 자동으로 메일 발송
```
## 2023.04.26(수) 파일 정리 완료
불필요한 파일 삭제
