from crawler import planner, harvester
from utils import utility
import threading
import concurrent.futures

stopEvent = threading.Event()

# URL 을 이용한 맵 생성의 경우
def runCrawlForMap(link):
    treeRoot = planner.initMap(link)
    tree = planner.writeDownMap(treeRoot)
    # tree = planner.writeDownMap_test(treeRoot)
    directoryName = harvester.getGalleryName(tree.root.url)
    directoryPath = utility.makeCrawlDir(directoryName)
    jsonFilePath = tree.saveTreeAsJson(directoryPath + '/' + 'map.json')
    return jsonFilePath

# MAP 파일을 이용한 실제 크롤링의 경우 (개선된 버전)
def runCrawlWithMap(mapFilePath, imageDirPath, numberOfThreads):
    # mapFilePath = projectDirPath + '/map.json'
    results = []
    print('mapFilePath : ', mapFilePath)
    parsedMapList = utility.parseMapFile(mapFilePath)
    if len(parsedMapList) == 0:
        print('No map file found in the directory or the file is empty. Please check the directory and the file.')
        return None
    else:
        # Make plan to crawl
        nubmerOfTotalArtworks = planner.getTotalArtworks(parsedMapList)
        unOccupiedArtworks = planner.getUnOccupiedArtworks(parsedMapList)
        if len(unOccupiedArtworks) == 0:
            print('All artworks are already crawled...')
            return mapFilePath
        
        print(f"[Overview] crawledArtworks / totalArtworks : ({nubmerOfTotalArtworks-len(unOccupiedArtworks)}/{nubmerOfTotalArtworks})")
        slicedMap = planner.sliceMap(unOccupiedArtworks, numberOfThreads)
        print(' length of Sliced map : ', len(slicedMap))
        
        # Multi threading start
        with concurrent.futures.ThreadPoolExecutor(max_workers=numberOfThreads) as executor:
            futures = []
            utility.clear_screen()
            for i in range(numberOfThreads):
                future = executor.submit(harvester.downloadArtWorks, numberOfThreads, i, slicedMap[i], imageDirPath, stopEvent)
                futures.append(future)
            try:
                for future in concurrent.futures.as_completed(futures):
                    results.extend(future.result())
            except KeyboardInterrupt:
                print("\n KeyboardInterrupt received, stopping workers.")
                stopEvent.set()
                concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)
                for future in futures:
                    results.extend(future.result())
            finally:
                # future 객체들이 완료될 때까지 기다리는 역할을 하며, 이 함수 자체가 future 객체들의 결과를 반환하지 않습니다. 
                print("Partial results collected:", len(results))
                updatedMapFilePath = utility.updateMapFile(results, mapFilePath)
                return updatedMapFilePath