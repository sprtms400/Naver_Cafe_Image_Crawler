## 네이버 카페 앨범 게시판 이미지 크롤러
네이버 카페의 앨범 게시판 에서 이미지를 추출 및 저장후 참고된 링크는 맵 형태로 저장하는 프로그램입니다.

링크는 트리 형태로 저장되어 추후 최신 업데이트된 자료에대해서 따로 관리 및 반영 하기에 용이합니다.

트리형태는 다음을 참조하세요.
![image](https://github.com/sprtms400/Naver_Cafe_Image_Crawler/assets/26298389/1e3a37c0-96d7-455d-8a65-1be83cd44a89)


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
#### 사용 예시
타겟 사이트 : https://cafe.naver.com/kumdibike?iframe_url=/ArticleList.nhn%3Fsearch.clubid=19039077%26search.menuid=80%26search.boardtype=I
![image](https://github.com/sprtms400/Naver_Cafe_Image_Crawler/assets/26298389/4c03f14b-4c73-4d2a-a357-d259e3e6a564)

#### 결과 예시
결과물로 카페명과, 게시판명, 시간정보가 기술된 디렉토리 생성 및 안에 map.json파일이 생성됩니다.
![image](https://github.com/sprtms400/Naver_Cafe_Image_Crawler/assets/26298389/a765b165-116b-458e-a0d9-56aa03498bd9)

### 4. 프로젝트의 실제 이미지 수집하기 (경로를 큰따옴표로 묶어주십시오) <br>
<i>해당 디렉토리 내에 map.json 파일이 필수적으로 존재해야 합니다. 없거나 손상됐을시 3번 과정으로 다시 돌아가십시오. <br>
최대 5개의 사용자가 스레드 숫자를 지정, 해당 수만큼 멀티스레드를 이용하여 빠르게 이미지 수집이 가능합니다 스레드 수는 해당 명령어 실행 후 선택하는 ui가 표출됩니다.</i>
```
python main.py <projectDirectoryPath>
```

#### 사용 예시
<3> 의 결과로 생성된 디렉토리를 지정하면 이미지 수집모드로 실행가능합니다. 다음의 사진을 참고하세요.
![image](https://github.com/sprtms400/Naver_Cafe_Image_Crawler/assets/26298389/5b798fc2-2dde-4713-96ef-f63348055fd2)

#### 결과 예시
작업이 시작되면 전달받은 스레드 갯수에따라 progress bar 가 생성됩니다.
![image](https://github.com/sprtms400/Naver_Cafe_Image_Crawler/assets/26298389/608ccd49-ea68-4599-8ef9-98a5f232f64a)

작업완료시 다음메세지와 함께 프로젝트 디렉토리의 images 디렉토리에 이미지들을 확인 할 수 있습니다.
이미지명은 map.json 의 'photoId' 와 동일합니다.
![image](https://github.com/sprtms400/Naver_Cafe_Image_Crawler/assets/26298389/3e300ac2-aa4e-454f-ab59-c338b2aedd47)

### 마라톤, 그란폰도 대회 이미지 검색 서비스에서의 담당부분
![image](https://github.com/sprtms400/Naver_Cafe_Image_Crawler/assets/26298389/e08e046b-7e1e-43c0-87c4-80f6261b067f)
본 리포지터리에서는 마라톤, 그란폰도 대회 이미지 검색 서비스에서 녹색 박스에 해당된 부분을 담당합니다. 프로젝트에 대한 자세한 설명은
다음 저장소를 확인하세요.
https://github.com/sprtms400/Granfondo_Photo_Search/tree/main
