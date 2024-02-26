## 네이버 카페 이미지 크롤러
네이버 카페 에서 이미지를 추출 및 저장후 참고된 링크는 맵 형태로 저장하는 프로그램입니다.
링크는 맵 형태로 저장되어 추후 최신 업데이트된 자료에대해서 따로 관리 및 반영 하기에 용이합니다.

## 개발된 환경

OS : Ubuntu 20.04

Python version : 3.9
``` conda create <project-name> python=3.9 ```

Chrome version : 121.0.6167.16

Chromedriver 는 Chrome의 버전과 동일하게 하여야합니다.
115 이후부터는 JSON형태로 endpoint를 제공하므로 다음의 사이트에서 Ctrl + F 로 버전을 검색해서 링크를 추출하십시오.
``` https://googlechromelabs.github.io/chrome-for-testing/known-good-versions-with-downloads.json ```


## 구조 설명
Gallery, Showroom, ArtPiece 세가지 타입으로 나누어 작동된다.