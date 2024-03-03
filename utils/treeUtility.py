from enum import Enum
from datetime import datetime
from utils.utility import genUUID
import json

# 노드 타입을 나타내는 열거형
class nodeType(Enum):
    GALLERY = 'gallery'
    SHOWROOM = 'showroom'
    ARTWORK = 'artwork'
    ROOT = 'root'

# 트리에 직접적으로 들어가는 노드 클래스
class TreeNode:
    def __init__(self, nodeType: nodeType, url: str):
        self.nodeId = genUUID()
        self.nodeType = nodeType
        self.url = url
        self.isConquered = False
        self.updatedDate = datetime.now()
        self.children = []
        self.parent = None
    
    def remove_child(self, child):
        # list comprehension을 이용하여 child가 아닌 노드들만 남기고 제거
        self.children = [ i for i in self.children if i is not child]
        
    def add_child(self, child):
        # 자식 노드를 중복성 검사 후 추가
        if not any(c.nodeId == child.nodeId for c in self.children):
            self.children.append(child)
            child.parent = self
        
    # def switch_parent(self, new_parent):
    #     if self.parent:
    #         self.parent(self)
    #     self.parent = new_parent
    #     new_parent.add_child(self)
        
    def exportNodeAsJson(self):
        # 노드를 JSON 형식으로 변환
        # export 시 자식노드는 nodeId만 반환한다.
        return {
            'nodeId': self.nodeId,
            'nodeType': self.nodeType,
            'url': self.url,
            'isConquered': self.isConquered,
            'updatedDate': self.updatedDate.isoformat() if self.updatedDate else None,  # datetime을 ISO 형식의 문자열로 변환,
            'childrenNodeId': [child.nodeId for child in self.children],
            'parentId': self.parent.nodeId if self.parent else None
        }

# 트리를 관리하는 클래스
class Tree:
    def __init__(self, root: TreeNode, treeName: str):
        self.root = root  # 그래프의 시작점인 헤드 노드
        self.treeName = treeName # 트리명
        
    # 깊이 우선 탐색을 사용한 트리 순회     
    def findNodeDFS(self, url, node=None):
        if node == None:
            node = self.root
        if node.url == url:
            return node
        for child in node.children:
            foundNode = self.findNodeDFS(url, child)
            if foundNode:
                return foundNode
        return None
            
    def getTreeNodes(self, node=None):
        # 재귀적으로 트리의 모든 노드를 리스트로 반환
        if node == None:
            # 노드가 주어지지 않으면 루트 노드부터 시작
            node = self.root
        nodes = [node]
        for child in node.children:
            nodes += self.getTreeNodes(child)
        return nodes
    
    def getConqueredNodes(self, node=None):
        if node == None:
            node = self.root
        conqueredNodes = []
        if node.isConquered:
            conqueredNodes.append(node)
        for child in node.children:
            conqueredNodes += self.getConqueredNodes(child)
        return conqueredNodes
    
    def getUnconqueredNodes(self, node=None):
        if node == None:
            node = self.root
        unconqueredNodes = []
        if not node.isConquered:
            unconqueredNodes.append(node)
        for child in node.children:
            unconqueredNodes += self.getUnconqueredNodes(child)
        return unconqueredNodes
    
    # def saveTreeAsJson(self, filePath):
    #     treeNodes = self.getTreeNodes()
    #     jsonifiedNodes = []
    #     for node in treeNodes:
    #         jsonifiedNodes.append(node.exportNodeAsJson())
    #     with open(filePath, 'w', encoding='utf-8') as f:
    #         # indent 옵션을 사용하여 들여쓰기를 적용
    #         json_str = json.dump(jsonifiedNodes, indent=4)
    #         f.write(json.dump(jsonifiedNodes, indent=4))
    
    def saveTreeAsJson(self, filePath):
        treeNodes = self.getTreeNodes()
        jsonifiedNodes = []
        for node in treeNodes:
            jsonifiedNodes.append(node.exportNodeAsJson())
        with open(filePath, 'w', encoding='utf-8') as f:
            # 여기에서 수정: f.write 메서드를 사용하지 않고, json.dump 함수로 직접 파일에 쓰기
            json.dump(jsonifiedNodes, f, indent=4)
        return filePath