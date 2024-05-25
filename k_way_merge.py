import heapq
def Merge_K_lists(arr):
    res = []
    min_heap = []

    #push every first (element, list_index, element_index) of all lists in arr to min_heap
    for idx, lis in enumerate(arr):
        if lis: #there might be empty lists
            heapq.heappush(min_heap, (lis[0], idx, 0))

    #pop the element from min_heap i.e., pop's minimum of heap and push to res
    while min_heap:
        val, lis_idx, val_idx = heapq.heappop(min_heap)
        res.append(val)

        # If there is a next element in the same list, push it into the heap
        if val_idx + 1 < len(arr[lis_idx]):
            heapq.heappush(min_heap, (arr[lis_idx][val_idx+1], lis_idx, val_idx+1))
    return res


arr = [sorted(list(map(int, input(f"Enter List-{i+1} Elements: ").split()))) \
        for i in range(int(input("Enter K: ")))] 
print(Merge_K_lists(arr))