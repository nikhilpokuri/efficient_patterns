'''
add some nodes to linked list
add the loop with the position(1-based index) in linkedlist
detect the loop is present or not
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
    def add_loop(self,data):
        if self.head is None:
            print("empty Linked List")
        else:
            lib = None
            if self.head.data == data:
                lib = self.head
                temp = self.head
                while temp.next:
                    temp = temp.next
                temp.next = lib
            else:
                temp = self.head.next
                print("Entered",temp.data)
                while temp.next:
                    if temp.data == data:
                        lib = temp
                    temp = temp.next
                if not lib:
                    lib = temp
                temp.next = lib

    def display(self):
        if self.head is None:
            print("Empty Linked List")
        else:
            temp = self.head
            lib = set()
            while temp and temp.next not in lib:
                print(temp.data, end=' ')
                lib.add(temp)
                temp = temp.next
            if temp and temp not in lib:
                print(temp.data) 
    def detect(self):
        if not self.head:
            return False
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow  = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

arr = list(map(int, input("Enter arr elements :").split()))
position = int(input("loop to number at: "))
l = LinkedList()
for i in arr:
    l.add_end(i)
if position > 0 and position <= len(arr):
    l.add_loop(arr[position-1])
print("Linked list:")
l.display()
print("Loop Existed:-",l.detect())