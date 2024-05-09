"""
            10
    3               30
2        4      20      40

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

targetSum = 80
def path_sum(root):
    stack = [[root, root.key]]
    while stack:
        node, curr_sum = stack.pop()
        # print(node.key,curr_sum)
        if node.left == None and node.right == None:
            if curr_sum == targetSum:
                return True
        if node.left:
            stack.append([node.left, curr_sum+node.left.key])
        if node.right:
            stack.append([node.right, curr_sum+node.right.key])
    return False
print(path_sum(root))