# data structure
# 'data' : {
#     'type': enum["gallery", "showroom", "artwork"],
#     'url': str,
#     'isConquered': bool,
#     'conqueredDate': date,
# }
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    
    def remove_child(self, child):
        # list comprehension을 이용하여 child가 아닌 노드들만 남기고 제거
        self.children = [
            i for i in self.children
                if i is not child
        ]
        
    def add_child(self, child):
        self.children.append(child)
        
    def switch_parent(self, new_parent):
        if self.parent:
            self.parent.remove_child(self)
        self.parent = new_parent
        new_parent.add_child(self)

class Tree:
    def __init__(self, root=None):
        self.root = root  # 그래프의 시작점인 헤드 노드
        
    # 깊이 우선 탐색을 사용한 트리 순회
    def traverse(self, node=None):
        if node is None:
            node = self.root
        print(node.data)  # 현재 노드의 데이터 출력
        for child in node.children:
            self.traverse(child)  # 재귀적으로 자식 노드 탐색
    
    def getTreeSize(self, node=None):
        if node is None:
            node = self.root
        size = 1
        for child in node.children:
            size += self.getTreeSize(child)
        return size
    
    def getConqueredNodes(self, node=None):
        if node is None:
            node = self.root
        conqueredNodes = []
        if node.data['isConquered']:
            conqueredNodes.append(node)
        for child in node.children:
            conqueredNodes += self.getConqueredNodes(child)
        return conqueredNodes
    
    def getUnconqueredNodes(self, node=None):
        if node is None:
            node = self.root
        unconqueredNodes = []
        if not node.data['isConquered']:
            unconqueredNodes.append(node)
        for child in node.children:
            unconqueredNodes += self.getUnconqueredNodes(child)
        return unconqueredNodes