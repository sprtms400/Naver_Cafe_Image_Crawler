#%%
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get('https://cafe.naver.com/kumdibike?iframe_url=/ArticleList.nhn%3Fsearch.clubid=19039077%26search.menuid=70%26search.boardtype=I')
time.sleep(2)
# elements = driver.find_elements(By.XPATH, '//*[@id="main-area"]/div[4]/a')
elements = driver.find_elements(By.CSS_SELECTOR, "#main-area > div.prev-next > a")
# print(elements)
print(elements)

#%%
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get('https://cafe.naver.com/kumdibike?iframe_url=/ArticleList.nhn%3Fsearch.clubid=19039077%26search.menuid=70%26search.boardtype=I')
time.sleep(2)
showRoomDoms = driver.find_elements(By.XPATH, '//*[@id="main-area"]/ul[1]/li')
print(showRoomDoms)

#%%
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get('https://www.google.com/')
searchbox = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')
print(searchbox)

#%%
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://cafe.naver.com/kumdibike?iframe_url=/ArticleList.nhn%3Fsearch.clubid=19039077%26search.menuid=70%26search.boardtype=I')

# iframe으로 전환 (중요)
driver.switch_to.frame("cafe_main")

# 이제 iframe 내부에서 요소를 찾을 수 있습니다.
elements = driver.find_elements(By.XPATH, '//*[@id="main-area"]/div[4]/a')

# 요소들의 처리...
elements