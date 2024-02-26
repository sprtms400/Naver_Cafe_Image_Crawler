from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver_path = './driver/chromedriver'

def driver_loader(driver_path):
    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service)
    return driver

def showAlbumForm(driver):
    # 자료를 앨범형으로 표출 (기본값이나 확인차 진행) 
    # WebDriverWait을 사용하여 요소가 클릭 가능할 때까지 최대 10초간 기다림
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div/div[2]/a[2]/span'))
    ).click()


# 게시판 내에 페이지링크들을 리스트 형태로 수집 및 반환하는 함수 
def galleryPageGatherer(galleryUrl):
    driver = driver_loader(driver_path)
    driver.get(galleryUrl)
    
    # 1. 자료를 앨범형으로 표출 (기본값이나 확인차 진행) 
    # driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div[2]/a[2]/span').click()
    showAlbumForm(driver)
    
    # 2. 게시판 내 pagenation된 페이지'들' 순번 링크 확보 
    gallaryPageElements = driver.find_elements(By.XPATH, '//*[@id="main-area"]/div[4]/a')
    galleryPageUrls = []
    for page in gallaryPageElements:
        galleryPageUrls.append(page.get_attribute('href'))
    return galleryPageUrls

# 게시판 페이지 내에 게시글 링크들을 리스트 형태로 수집 및 반환하는 함수
def harvestShowRoomUrls(galleryUrl):
    driver = driver_loader(driver_path)
    driver.get(galleryUrl)
    
    # 1. 자료를 앨범형으로 표출 (기본값이나 확인차 진행) 
    # driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div[2]/a[2]/span').click()
    showAlbumForm(driver)
    
    # 2. 게시판 내 게시글 링크들 확보
    showRoomUrls = driver.find_elements(By.XPATH, '//*[@id="main-area"]/ul[1]/li')
    return showRoomUrls

def harvestArtWork(showRoomUrl):
    driver = driver_loader(driver_path)
    driver.get(showRoomUrl)
    # 1. 게시글 내 이미지들 DOM 확보
    artWorks = driver.find_elements(By.XPATH, '//div[@class="se-component se-image se-l-default"]/div/div/div/a/img')
    return []