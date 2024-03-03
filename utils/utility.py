import uuid
import os
import json
import time
import sys

from datetime import datetime

def makeDir(dirPath):
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)
    return dirPath

def makeCrawlDir(cafeName):
    dirPath = cafeName + '_' + datetime.now().strftime('%Y-%m-%d_%H:%M')
    return makeDir(dirPath)

def parseMapFile(mapFilePath):
    mapList = []
    if os.path.exists(mapFilePath):
        with open(mapFilePath, 'r', encoding='utf-8') as file:
            mapList = json.load(file)
    return mapList
    
def genUUID():
    # uuid 생성
    uuid_val = uuid.uuid4()

    # Convert UUID to integer
    # uuid_int = int(uuid_val.hex, 16)
    # uuid_val.hex 는 단지 중간의 하이픈만을 없앤것이다.
    return uuid_val.hex

def readOrder(orderListFilePath):
    orders = []
    with open(orderListFilePath, 'r') as f:
        orders = f.readlines()
    orders = [order.strip() for order in orders]
    return orders

def clear_screen():
    # 운영 체제 확인
    os_name = os.name
    if os_name == 'nt':  # Windows
        os.system('cls')
    else:  # UNIX/Linux/macOS
        os.system('clear')

def print_progress_bar_by_workerNumber(workerNumber, iteration, total, prefix='', suffix='', length=100, fill='█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        workerNumber- Optional  : worker number (Int)
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    sys.stdout.write('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix)),
    # Print New Line on Complete
    if iteration == total: 
        print()

def move_cursor(x, y):
    print(f"\033[{y};{x}H", end='')

def get_terminal_height():
    return os.get_terminal_size().lines

def displayMultipleProgressBars(numberOfWorkers, workerNumber, iteration, total, prefix='', suffix='', length=50, fill='█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        workerNumber- Optional  : worker number (Int)
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    terminal_height = get_terminal_height()
    cursor_y_position = terminal_height - numberOfWorkers + workerNumber
    move_cursor(0, cursor_y_position)
    sys.stdout.write('\r%s |%s| %s%% %s \n' % (prefix, bar, percent, suffix)),
    if iteration == total: 
        print()

def updateMapFile(results, mapFilePath):
    try:
        # 파일 존재 확인
        if not os.path.exists(mapFilePath):
            return None
        # Map 파일 읽기
        with open(mapFilePath, 'r', encoding='utf-8') as file:
            mapList = json.load(file)
        # 결과를 nodeId를 키로 하는 딕셔너리로 변환
        resultsDict = {result['nodeId']: result for result in results}
        # mapList 업데이트
        updated = False
        for mapItem in mapList:
            nodeId = mapItem['nodeId']
            if nodeId in resultsDict:
                result = resultsDict[nodeId]
                mapItem['isConquered'] = result['isConquered']
                mapItem['updatedDate'] = result['updatedDate'].isoformat() if isinstance(result['updatedDate'], datetime) else result['updatedDate']
                updated = True
        # 업데이트된 경우, 파일 쓰기
        if updated:
            with open(mapFilePath, 'w', encoding='utf-8') as f:
                json.dump(mapList, f, ensure_ascii=False, indent=4)
            print('Map file updated successfully.')
        else:
            print('No updates applied to the map file.')
        return mapFilePath
    except Exception as e:
        print('Error occurred while updating the map file:', e)
        return None

def checkURL(url):
    if url.startswith('http://') or url.startswith('https://'):
        return True
    else:
        return False
    
def checkPath(directoryPath):
    if os.path.exists(directoryPath):
        return True
    else:
        return False