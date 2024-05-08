"""
            10
    3               30
2        4      20      40
Answer: [[10],[3,30],[2,4,20,40]]
""" 
class BST:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def add_node(self, data):
        if self.key == None:
            self.key = data
        elif self.key == data:
            return
        else:
            if data < self.key:
                if self.left:
                    self.left.add_node(data)
                else:
                    self.left = BST(data)
                
            if data > self.key:
                if self.right:
                    self.right.add_node(data)
                else:
                    self.right = BST(data)
                
    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.key)
        if self.right:
            self.right.inorder()
    
            
arr = [10,3,30,2,4,20,40]
root = BST(arr[0])
for i in arr[1:]:
    root.add_node(i)
# root.inorder()


from collections import deque
def bfs(root):
    queue = deque()
    queue.append([root])
    res = [[root.key]]
    while queue:
        nodes = queue.popleft()
        tmp1 = []
        tmp2 = []
        for node in nodes:
            if node.left:
                tmp1.append(node.left)
                tmp2.append(node.left.key)
            if node.right:
                tmp1.append(node.right)
                tmp2.append(node.right.key)
        if tmp1:
            queue.append(tmp1)
        if tmp2:
            res.append(tmp2)
    return res
print(bfs(root))
 