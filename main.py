#%%
import sys
import ui.mainUi as mainUi
import utils.utility as utility
if __name__ == "__main__":
    if len(sys.argv) < 2: # 파라미터 검사
        print('Usage: python main.py [List of URLs.txt] or [Path of Directory wich contains \'map.json\']')
        sys.exit (1) # 사용법 안내 후 종료
    if utility.checkPath(sys.argv[1]): # 경로 검사
        print('Start crawling with map file...')
        mainUi.landingUIwithMap(sys.argv[1])
    elif utility.checkURL(sys.argv[1]): # URL 리스트 검사
        print('Start crawling to make map file...')
        mainUi.landingUIforMap(sys.argv[1])
    else:
        print('Invalid input')
        sys.exit (1)