from crawler import core
import utils.utility as utility

# URL 을 이용한 맵 생성의 경우
def landingUIforMap(url):
    while True:
        print('Target URL :', url)
        print('After crawling for make \'map.json\' file, The \'map.json\' file will be saved in new directory')
        print('This is not the actual crawling, but the map creation for the crawling')
        option = input('Try crawl to make \'map.json\' file? (y/n) >>')
        if option == 'y' or option == 'Y':
            print('You can stop the program by pressing Ctrl+C, It will save the current state of the map.\n' +
                  'But it may not be able to resume the crawling from the point where it stopped')
            print('Start crawling to make \'map.json\'...')
            dirPath = core.runCrawlForMap(url)   
            print(f"The map file maded at ... {dirPath}")
            return dirPath
        elif option == 'n' or option == 'N' or option == 'q':
            print('Program terminated...')
            return None
        else :
            print('Invalid input')
            continue

# MAP 파일을 이용한 맵 생성의 경우
def landingUIwithMap(directoryPath):
    # make images directory
    imageDirPath = utility.makeDir(directoryPath + '/images')
    mapFilePath = directoryPath + '/map.json'
    if not utility.checkPath(mapFilePath):
        print('No \'map.json\' file found in the directory. Please check the directory and the file.')
        return None
    while True:
        print('Target map file is :', mapFilePath)
        print('This is the actual crawling with the \'map.json\' file you can use multiple threads to crawl')
        option = input(f"Try crawl with \'map.json\' file at {mapFilePath}? (y/n) >>")
        if option == 'y' or option == 'Y':
            print('You can stop the program by pressing Ctrl+C, It will save the current state of the map.\n' +
                  'But it may not be able to resume the crawling from the point where it stopped')
            numOfThreads = input('How many threads do you want to use? (1~5) >>')
            print(f"Start crawling with {numOfThreads} threads...")
            dirPath = core.runCrawlWithMap(mapFilePath, imageDirPath, int(numOfThreads))
            print(f"Crawling finished, The map file updated at ...{dirPath}")
            return dirPath
        elif option == 'n' or option == 'N' or option == 'q':
            print('Program terminated...')
            return None
        else :
            print('Invalid input')
            continue