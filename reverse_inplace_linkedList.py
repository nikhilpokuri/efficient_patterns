class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add_node(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node 
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
    
    def reverse_LL(self):
        prev = None
        temp = self.head
        while temp:
            next_node = temp.next
            temp.next = prev
            prev = temp
            temp = next_node
            self.head = prev
        return self.head

    def display(self):
        if not self.head:
            print('Linked List is empty')
            return
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

arr = [1,2,3,4,5]
obj = LinkedList()
for i in arr:
    obj.add_node(i)
obj.reverse_LL()
obj.display()