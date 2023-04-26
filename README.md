# 1. 실행되기 위한 조건

### (조건1) 디렉토리 위치 설정
```
깃허브에서 다운로드 시, C드라이브 아래에 'flyordig' 라는 폴더를 만들고
그 폴더에 cafe_crawling이라는 폴더에 모든 파일이 있어야 함.

다운로드 위치
C:\flyordig\cafe_crawling\
```
```
※ 폴더 위치를 지정해야하는 이유
    - cr.py가 크롤링한 엑셀 파일의 위치를 proc.py와 mailing.py에서 참조하기 때문  
```

### (조건2) 파일확인
```
- 파일 목록
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
### (조건3) 모듈 설치
```
pip install selenium openpyxl pyperclip python-dateutil beautifulsoup4 pandas requests pyautogui
```
cmd(명령프롬프트)에 상기의 명령어를 입력하여 모듈 다운로드


# 2. 함수 설명
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

# 3. 이력
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
