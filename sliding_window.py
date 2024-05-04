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
arr = list(map(int,input("enter arr elements: ").split()))
K = int(input("Enter SubArr size: "))
N = len(arr)
print(maximumSumSubarray(K,arr,N))