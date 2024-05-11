def maximumSumSubarray (K,arr,N):
    if K == 1:
        return max(arr)
    if N == 1:
        return arr[0]
    curr_maxi = 0
    result = 0
    for i in range(K):
        curr_maxi += arr[i]
        result += arr[i]
    start = 0
    end = K
    while end < N :
        new_maxi = (curr_maxi-arr[start]) + arr[end]
        result = max(result, new_maxi)
        curr_maxi = new_maxi
        start += 1
        end += 1
    return result

def slidingWindowMaximum(K,arr,N):
    import heapq
    # arr = [9,3,-1,4,5,3,6,7]
    # arr = [1,3,-1,-3,5,3,6,7]
    # arr = [1,9,-1,4,5,3]
    k = 3
    tmp = []
    res = []
    for i in range(k):
        heapq.heappush(tmp, [-arr[i],i])
    res.append(-tmp[0][0])

    for i in range(k, len(arr)):
        heapq.heappush(tmp, [-arr[i],i])
        while tmp[0][1] <= i-k:
            #remove first element in window if it's not in between nums[i:i+k],
            # bcoz first element is maximum in window, we will allow only windows's max as window[0]
            heapq.heappop(tmp)
        res.append(-tmp[0][0])
    return res

arr = list(map(int,input("enter arr elements: ").split()))
K = int(input("Enter SubArr size: "))
N = len(arr)
print("maximumSumSubarray:",maximumSumSubarray(K, arr, N))
print("slidingWindowMaximum:",slidingWindowMaximum(K, arr, N))
