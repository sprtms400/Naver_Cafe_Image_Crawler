from utils.treeUtility import Tree, TreeNode
from utils.utility import genUUID
import crawler.harvester as harvester
import os

def readOrder(orderListFilePath):
    orders = []
    with open(orderListFilePath, 'r') as f:
        orders = f.readlines()
    orders = [order.strip() for order in orders]
    return orders

def initMaps(orderListFilePath):
    targetGalleries = readOrder(orderListFilePath)
    trees = []
    for targetGallery in targetGalleries:
        rootNode = TreeNode(nodeType='root', url=targetGallery)
        trees.append(Tree(root=rootNode, treeName=targetGallery))
    return trees

def writeDownMap(tree: Tree):
    try: 
        rootNode = tree.root
        
        # 게시판 페이지네이션 된 페이지들 수집.
        galleryPageUrls = harvester.exploreGalleryPageUrls(rootNode.url)

        for galleryPageUrl in galleryPageUrls:
            galleryPage = TreeNode(nodeType='gallery', url=galleryPageUrl)
            # galleryPage.switch_parent(rootNode)
            rootNode.add_child(galleryPage)

            # 페이지 내의 게시글들 수집
            showRoomUrls = harvester.harvestShowRoomUrls(galleryPageUrl)
            
            for showRoomUrl in showRoomUrls:
                showRoom = TreeNode(nodeType='showroom', url=showRoomUrl)
                # showRoom.switch_parent(galleryPage)
                galleryPage.add_child(showRoom)
                
                # 게시글 내의 이미지들 수집
                artWorkUrls = harvester.harvestArtWorkUrls(showRoomUrl)
                for artWorkUrl in artWorkUrls:
                    artWork = TreeNode(nodeType='artwork', url=artWorkUrl)
                    showRoom.add_child(artWork)
                    # artWork.switch_parent(showRoom)
        return tree
    except KeyboardInterrupt:
        print('Halted drawing the map')
        return tree
    except Exception as e:
        print('Error occured while drawing the map', e)
        return tree
    
# def writeDownMap(tree: Tree):
#     rootNode = tree.root
    
#     # 게시판 페이지네이션 된 페이지들 수집.
#     galleryPageUrls = harvester.exploreGalleryPageUrls(rootNode.url)

#     for galleryPageUrl in galleryPageUrls:
#         galleryPage = TreeNode(nodeType='gallery', url=galleryPageUrl)
#         # galleryPage.switch_parent(rootNode)
#         rootNode.add_child(galleryPage)

#         # 페이지 내의 게시글들 수집
#         showRoomUrls = harvester.harvestShowRoomUrls(galleryPageUrl)
        
#         for showRoomUrl in showRoomUrls:
#             showRoom = TreeNode(nodeType='showroom', url=showRoomUrl)
#             # showRoom.switch_parent(galleryPage)
#             galleryPage.add_child(showRoom)
            
#             # 게시글 내의 이미지들 수집
#             artWorkUrls = harvester.harvestArtWorkUrls(showRoomUrl)
#             for artWorkUrl in artWorkUrls:
#                 artWork = TreeNode(nodeType='artwork', url=artWorkUrl)
#                 showRoom.add_child(artWork)
#                 # artWork.switch_parent(showRoom)
#     return tree