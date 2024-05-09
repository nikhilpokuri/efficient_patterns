import heapq
class FindMedian:
    def __init__(self):
        self.small = []
        self.large = []
    
    def push(self,num):
        heapq.heappush(self.small, -1*num) #add to small(max_heap) with -1*num to maintain max_heap
        # print(small, large)
        if self.small and self.large and -1*self.small[0] > self.large[0]:
            tmp = heapq.heappop(self.small)
            heapq.heappush(self.large,-1*tmp)

        if len(self.small) - len(self.large) > 1:
            tmp = heapq.heappop(self.small)
            heapq.heappush(self.large, -1*tmp)
        if len(self.large) - len(self.small) > 1:
            tmp = heapq.heappop(self.large)
            heapq.heappush(self.small, -1*tmp)

    def median(self):
        if not self.small and not self.large:
            return None
        if len(self.small) > len(self.large):
            return -1*self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return (-1*self.small[0] + self.large[0])/2
small = [] #max_heap
large = [] #min_heap
obj = FindMedian()
while True:
    operation = input("Operation['push', 'median', 'exit']: ")
    if operation.lower() == 'exit':
        break
    elif operation.lower() == 'push':
        num = int(input("Enter Number: "))
        obj.push(num)
    elif operation.lower() == 'median':
        print(obj.median())
    else:
        print("Invalid Operation")