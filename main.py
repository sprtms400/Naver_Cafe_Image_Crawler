#%%
from crawler import planner, harvester
from utils.utility import makeCrawlDir
import time

links = planner.initMaps('orderURLs.txt')
tree = None
for link in links:
    tree = planner.writeDownMap(link)
    print(link.root.url)
    directoryName = harvester.getGalleryName(link.root.url)
    directoryPath = makeCrawlDir(directoryName)
    tree.saveTreeAsJson(directoryPath + '/' + 'tree.json')
tree.getTreeNodes()
