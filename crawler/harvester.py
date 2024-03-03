from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

import utils.utility as utility
import time
import re
import requests



DRIVER_PATH = './driver/chromedriver'

def driver_loader(driver_path):
    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service)
    return driver

def showAlbumForm(driver):
    # 자료를 앨범형으로 표출 (기본값이나 확인차 진행) 
    # WebDriverWait을 사용하여 요소가 클릭 가능할 때까지 최대 10초간 기다림
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="main-area"]/div[2]/div/div[2]/a[2]'))
    ).click()


# 게시판 내에 페이지링크들을 리스트 형태로 수집 및 반환하는 함수 
def exploreGalleryPageUrls(partOfGalleryUrl):
    driver = driver_loader(DRIVER_PATH)
    driver.get(partOfGalleryUrl)
    wait = WebDriverWait(driver, 10)  # 10초 동안 기다림
    
    # 1. ifream으로 전환 (중요)
    time.sleep(3)
    driver.switch_to.frame('cafe_main')
    # wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, 'cafe_main')))
    
    # 2. 자료를 앨범형으로 표출 (기본값이나 확인차 진행) 
    # showAlbumForm(driver)
    
    # 3. 게시판 내 pagenation된 페이지'들' 순번 링크 확보
    # gallaryPageElements = driver.find_elements(By.XPATH, '//*[@id="main-area"]/div[4]/a')
    gallaryPageElements = wait.until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@id="main-area"]/div[4]/a')))

    wholeGalleryPageUrls = []
    for page in gallaryPageElements:
        wholeGalleryPageUrls.append(page.get_attribute('href'))
    driver.quit()
    return wholeGalleryPageUrls

# 게시판 페이지 내에 게시글 링크들을 리스트 형태로 수집 및 반환하는 함수
def harvestShowRoomUrls(galleryUrl):
    driver = driver_loader(DRIVER_PATH)
    driver.get(galleryUrl)
    wait = WebDriverWait(driver, 10)  # 10초 동안 기다림

    # 1. ifream으로 전환 (중요)
    time.sleep(3)
    driver.switch_to.frame('cafe_main')
    # wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, 'cafe_main')))
    
    # 2. 자료를 앨범형으로 표출 (기본값이나 확인차 진행) 
    # showAlbumForm(driver)
    
    # 3. 게시판 내 게시글 링크들 확보
    showRoomDoms = wait.until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@id="main-area"]/ul[1]/li/a')))
    # showRoomDoms = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'album-img')))
    showRoomUrls = []

    for showRoomDom in showRoomDoms:
        showRoomUrls.append(showRoomDom.get_attribute('href'))

    driver.quit()
    return showRoomUrls

def harvestArtWorkUrls(showRoomUrl):
    driver = driver_loader(DRIVER_PATH)
    driver.get(showRoomUrl)
    wait = WebDriverWait(driver, 10)  # 10초 동안 기다림
    
    # 1. ifream으로 전환 (중요)
    time.sleep(3)
    driver.switch_to.frame('cafe_main')
    # wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, 'cafe_main')))
    
    # 2. 게시글 내 이미지 링크들 확보
    artWorkDoms = wait.until(EC.visibility_of_all_elements_located((By.XPATH, '//div[@class="se-component se-image se-l-default"]/div/div/div/a/img')))

    artWorkUrls = []
    for artWorkDom in artWorkDoms:
        artWorkUrls.append(artWorkDom.get_attribute('src'))
    driver.quit()
    return artWorkUrls

def getGalleryName(galleryUrl):
    driver = driver_loader(DRIVER_PATH)
    driver.get(galleryUrl)
    wait = WebDriverWait(driver, 10)  # 10초 동안 기다림
    
    # 1. ifream으로 전환 (중요)
    time.sleep(3)
    driver.switch_to.frame('cafe_main')
    # wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, 'cafe_main')))
    
    # 2. 카페명, 게시판 이름 획득
    cafeName = re.search(r'cafe\.naver\.com/([^/?]+)', galleryUrl).group(1)
    galleryName = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="sub-tit"]/div[1]/div/h3'))).text
    driver.quit()
    return cafeName + '_' + galleryName.replace(' ', '_')

def downloadArtWork(artWorkUrl, downloadPath):
    response = requests.get(artWorkUrl)
    if response.status_code == 200:
        with open(downloadPath, 'wb') as file:
            file.write(response.content)
        return downloadPath
    else:
        return None

def downloadArtWorks(numberOfWorkers, workerNumber, targets, saveDir, stopEvent):
    try:
        checkList = []
        i = 0
        for target in targets:
            if stopEvent.is_set():
                print(f" --> Worker {workerNumber} stopping.")
                return checkList
            targetUrl = target['url']
            downloadPath = f"{saveDir}/{target['nodeId']}"
            if downloadArtWork(targetUrl, downloadPath) != None:
                checkList.append({
                    'nodeId': target['nodeId'],
                    'nodeType': target['nodeType'],
                    'url': target['url'],
                    'isConquered': True,
                    'updatedDate': datetime.now(),
                    'childrenNodeId': target['childrenNodeId'],
                    'parentId': target['parentId']
                })
            i += 1
            
            utility.displayMultipleProgressBars(numberOfWorkers=numberOfWorkers, workerNumber=workerNumber, iteration=i, 
                                                    total=len(targets), prefix=f"Worker ({workerNumber+1}) Progress:", suffix='Complete:', length=50)
        return checkList
    except Exception as e:
        print('Error occured while downloading the artworks', e)
        return checkList