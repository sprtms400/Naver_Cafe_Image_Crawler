#%%
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# ChromeDriver의 경로 지정
driver_path = './driver/chromedriver'
service = Service(executable_path=driver_path)
browser = webdriver.Chrome(service=service)

# 웹사이트 열기
browser.get('https://cafe.naver.com/kumdibike?iframe_url=/ArticleList.nhn%3Fsearch.clubid=19039077%26search.menuid=70%26search.boardtype=I')

#%%
import threading
from queue import Queue
from utils import parser

if __name__ == "__main__":
    file_path = './galleries.txt'
    galleries = parser.parse_galleries_file(file_path)