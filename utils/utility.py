import uuid
import os
import json
from datetime import datetime

def makeCrawlDir(cafeName):
    dirPath = cafeName + '_' + datetime.now().strftime('%Y-%m-%d_%H:%M')
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)
    return dirPath

def parseGalleriesFile(file_path):
    galleries = []  # 결과를 저장할 배열
    try:
        with open(file_path, 'r') as file:  # 파일을 읽기 모드로 열기
            for line in file:  # 파일의 각 줄에 대해 반복
                # 줄바꿈 문자를 제거하고 배열에 추가
                galleries.append(line.strip())
    except FileNotFoundError:
        print(f"파일을 찾을 수 없습니다: {file_path}")
    except Exception as e:
        print(f"파일을 읽는 동안 오류가 발생했습니다: {e}")
    return galleries

def genUUID():
    # uuid 생성
    uuid_val = uuid.uuid4()

    # Convert UUID to integer
    # uuid_int = int(uuid_val.hex, 16)
    # uuid_val.hex 는 단지 중간의 하이픈만을 없앤것이다.
    return uuid_val.hex