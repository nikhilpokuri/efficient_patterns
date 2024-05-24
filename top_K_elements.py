import heapq

def top_k_elements(arr, k):
    if k == len(arr):
        return sorted(arr, reverse=True), sorted(arr)

    if k > len(arr):
        raise Exception("K value constraint 0 < k <= len(arr)")
    min_heap = [] #to store top k large elements
    max_heap = [] # to store top k small elements
    for i in arr:
        heapq.heappush(min_heap, i)
        heapq.heappush(max_heap, -i)

        if len(min_heap) > k:
            heapq.heappop(min_heap)
        if len(max_heap) > k:
            heapq.heappop(max_heap)

    min_heap.sort(reverse=True)
    max_heap.sort()
    return min_heap, max_heap

arr = list(map(int, input("Elements: ").split()))
k = int(input("K: "))
min_heap, max_heap = top_k_elements(arr, k)
print('Top K Large Elements:', min_heap)
print('Top K Small Elements:', list(map(abs, max_heap)))