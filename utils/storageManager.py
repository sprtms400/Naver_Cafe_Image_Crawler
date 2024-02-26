import os
from datetime import datetime

def makeCrawlDir(cafeName):
    dirPath = cafeName + datetime.now().strftime('%Y-%m-%d_%H:%M')
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)
    return dirPath