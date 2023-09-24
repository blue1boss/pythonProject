'''

이진트리(binary Tree)
    모든 노드가 최대 2개의 자식 노드를 가질 수 있는 구조를 말한다.
    왼쪽 서브 트리의 값은 루트의 값보다 작고 오른쪽은 커지도록 구성된다.
'''
class TreeNode:
    def __init__(self, value):
        self.value = value # 노드의 값
        self.left = None # 왼쪽 서브트리 노드
        self.right = None # 오른쪽 서브트리 노드

class BinaryTree:
    def __init__(self, root):
        self.root = TreeNode(root) # 루트노드 , 트리노드 생성하여 값 저장

#전위순회 root- left -right
    '''
    1.
    preorder_traversal(bt.root, "") 
    bt.root = Node(5) 
    start = Node(5) 
    traversal  = "5#"
      2-1  preorder_traversal(Node(3), "5#")
        start = Node(3) 
        traversal = "5#3#"        <- #5#3#4#2#
        
        레프로 하면 Node(2) 로 간다. 
        3-1. preorder_traversal(Node(2), "5#3#")
        start = Node(2) 
        traversal = "5#3#2#"
        
        레프트가 없어서 none preorder_traversal(Node(2), "5#3#2#")
            4-1.
            preorder_traversal(None, "5#3#2#") 
            4-2.
            preorder_traversal(None, "5#3#2#") 
            
            3-2.
            preorder_traversal(Node(4), traversal)
             start= Node(4)
             traversal= "5#3#2#4#"
             
             4-1
                preorder_traversal(, "5#3#2#4#")
                preorder_traversal(, "5#3#2#4#")
            
        2-2 
        preorder_travesral(Node(7), "5#3#2#4#"
        start = Node(7)
        traversal = "5#3#2#4#7#"
            preorder_travesral(Node(6), "5#3#2#4#7#")
            start= Node(6)
            traversal=  "5#3#2#4#7#6#"
            
        preorder_traversal(Node(8), "5#3#2#4#7#6#")
        start = Node(8)
        traversal= "5#3#2#4#7#6#8#"
            
    '''

    '''
    
     def inorder_traversal(self, start, traversal):
        if start:
            traversal = self.inorder_traversal(start.left, traversal)
            traversal += (str(start.value)+ '#')
            traversal = self.inorder_traversal(start.right, traversal)
            
    *중위순위: left- root -right
    1. 
    inorder_traversal(bt.root,"")) 
    bt.root = Node(5) 
    start = Node(5)
    traversal = ""
        2-1
        inorder_traversal(Node(3), traversal) 
        start = Node(3) 
        traversal= ""
            3-1. 
            inorder_traversal(Node(2), "")
            start = Node(2)
            traversal = "2#"
            4-1. 
            inorder_traversal(None,"") => "" left
            4-2. 
            inorder_traversal(None,"2#") => "2#" 노드 2 왼쪽 없음 오른쪽 가는것임
         inorder_traversal(Node(4), "2#3#")
            start = Node(4)
            traversal = "2#3#"
            
            
    '''
    def preorder_traversal(self, start, traversal):
        if start:
            traversal += (str(start.value) + '#')

            traversal = self.preorder_traversal(start.left, traversal)

            traversal = self.preorder_traversal(start.right, traversal)
        return traversal

    def inorder_traversal(self, start, traversal):
        if start:
            traversal = self.inorder_traversal(start.left, traversal)
            traversal += (str(start.value)+ '#')
            traversal = self.inorder_traversal(start.right, traversal)
        return traversal

    # 후위순회 left -> right -> root
    def postorder_traversal(self, start, traversal):
        if start:
            traversal = self.postorder_traversal(start.left, traversal)
            traversal = self.postorder_traversal(start.right, traversal)
            traversal += (str(start.value) + ' ')
        return traversal

    def search(self, value):
        return self._search(value, self.root)

    def _search(self, value, current_node):
        if not current_node:
            return False
        elif current_node.value == value:
            return True
        elif value < current_node.value:
            return self._search(value, current_node.left)
        else:
            return self._search(value, current_node.right)

    # 삽입 메소드 : 이진 탐색을 사용하여 새 노드를 삽입
'''
3 7 2 4 6 8
Node(5).left -> Node(3)
        .right -> None 
        
insert(3)의 경우 

insert(3) -> Node(5).left -> Node(3) 
    _insert(3,Node(5))
    value = 3
    current_node= Node(5)
    current_node.left = Node(3)    

3 실행까지 실행하고
insert(7)

insert(7) -> Node(5).left -> Node(3) 
    _insert(7,Node(5))
    value = 7 (7이 더 크기에 elif의 함수가 실행) 
    current_node= Node(5)
    current_node.right = Node(7)  

7실행이후 

insert(2)
    _insert(2,Node(5))
    value = 2 (작기 때문에 앞쪽의 함수가 실행) 
    current_node= Node(5) #5의 레프트가 3이 이미 있음 -> else쪽으로 실행이 바로 된다는 것이다. 
    current_node = Node(5)  
    _insert(2, node(3)) #left값이 들어가기에 
    value = 2
    current_node= Node(3)
    current_node.let
    
    
    전위 순회는 왼쪽부터 싹 내려가서 먼저, 레프트가 업다면 subtree의 루트로 가서 마지막 오른쪽으로 이동한다. 
    중의 : 레프트- 중간 - 오른쪽 - 조금 더 큰 루트 & 반복 - 원본 루트 - 아래 -중간ㄴ
'''
    def insert(self, value): #3값들어감
        if not self.root: #none이면 true
            self.root = TreeNode(value)
        else:
            self._insert(value, self.root)


    def _insert(self, value, current_node):
        if value < current_node.value:
            if not current_node.left:   # current_node.left 값이 None 실행
                current_node.left = TreeNode(value)
            else:
                self._insert(value, current_node.left)

        elif value > current_node.value:

            if not current_node.right:
                current_node.right = TreeNode(value)
            else:
                self._insert(value, current_node.right)
        else:
            print('이미 존재하는 값입니다.')

    def delete(self, value):
        if not self.root:
            return
        else:
            self.root = self._delete(value, self.root)

    def _delete(self, value, current_node):
        if not current_node:
            return current_node
        elif value < current_node.value:
            current_node.left = self._delete(value, current_node.left)
        elif value > current_node.value:
            current_node.right = self._delete(value, current_node.right)
        else:
            if not current_node.left and not current_node.right:
                current_node = None
            elif not current_node.left:
                current_node = current_node.right
            elif not current_node.right:
                current_node = current_node.left
            else:
                min_node = self._find_min(current_node.right)
                current_node.value = min_node.value
                current_node.right = self._delete(min_node.value, current_node.right)

        return current_node

    def _find_min(self, current_node):
        while current_node.left:
            current_node = current_node.left
        return current_node

# 실행 코드
bt = BinaryTree(5) # 루트 노드 5인 이진트리 객체 생성

# 값 삽입
bt.insert(3)
bt.insert(7)
bt.insert(2)
bt.insert(4)
bt.insert(6)
bt.insert(8)

# 이진 트리를 전위 순회한 결과 출력
print('전위 순회: ', bt.preorder_traversal(bt.root, ""))

# 이진 트리를 중위 순회한 결과 출력
print('중위 순회: ', bt.inorder_traversal(bt.root, ""))

# 이진 트리를 후위 순회한 결과 출력
print('후위 순회: ', bt.postorder_traversal(bt.root, ""))

# 값 검색
print('값 4가 트리에 존재하는가? ', bt.search(4))
print('값 9가 트리에 존재하는가? ', bt.search(9))

# 값 삭제
bt.delete(3)
print('값 3을 삭제한 후 중위 순회: ', bt.inorder_traversal(bt.root, ""))