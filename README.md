## 네이버 카페 앨범 게시판 이미지 크롤러
네이버 카페의 앨범 게시판 에서 이미지를 추출 및 저장후 참고된 링크는 맵 형태로 저장하는 프로그램입니다.

링크는 맵 형태로 저장되어 추후 최신 업데이트된 자료에대해서 따로 관리 및 반영 하기에 용이합니다.

:o:게시판 단위로 크롤링되기때문에 앨범 게시판 링크를 전달해야합니다.:o:

:x:카페링크 전달시 작동하지 않습니다.:x:

## 개발된 환경 및 구성

OS : Ubuntu 20.04

Python version : 3.9
``` 
conda create <project-name> python=3.9
```

Chrome version : 121.0.6167.16

Chromedriver 는 Chrome의 버전과 동일하게 하여야합니다.
115 이후부터는 JSON형태로 endpoint를 제공하므로 다음의 사이트에서 Ctrl + F 로 버전을 검색해서 링크를 추출하십시오.
``` 
https://googlechromelabs.github.io/chrome-for-testing/known-good-versions-with-downloads.json
```
## 셋업 및 사용법
### 1. Chromedriver 위치시키기 <br>
<i>환경구성에서 다운로드 받은 chromedriver 파일을 프로젝트 디렉토리 내 driver 디렉토리로 위치시키십시오</i>
```
  cp chromedriver ./driver/
```
### 2. 의존 라이브러리 설치
```
pip install -r requirements.txt
```

### 3. 프로젝트 생성 및 map.json 생성 (링크를 큰따옴표로 묶어주십시오) <br>
<i>해당 과정 이후 프로젝트 디렉토리가 자동 생성 및 안에 map.json 파일이 생깁니다.<br>
주소는 게시판 
</i>
```
python main.py <"Navercafe 게시판 주소">
```

### 4. 프로젝트의 실제 이미지 수집하기 (경로를 큰따옴표로 묶어주십시오) <br>
<i>해당 디렉토리 내에 map.json 파일이 필수적으로 존재해야 합니다. 없거나 손상됐을시 3번 과정으로 다시 돌아가십시오. <br>
최대 5개의 사용자가 스레드 숫자를 지정, 해당 수만큼 멀티스레드를 이용하여 빠르게 이미지 수집이 가능합니다 스레드 수는 해당 명령어 실행 후 선택하는 ui가 표출됩니다.</i>
```
python main.py <projectDirectoryPath>
```

# 사용예시
