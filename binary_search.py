def BinarySearch(arr, k):
    n = len(arr)
    m_ind = n // 2
    print(m_ind)
    if k == arr[m_ind]:
        return "Found At Middle"
    elif k < m_ind:
        for i in range(0, m_ind):
            if arr[i] == k:
                return "Found Before Middle"
    else:
        for i in range(m_ind+1, n):
            if arr[i] == k:
                return "Found After Middle"
    return "Not Found"
print(BinarySearch([1,2,3,4,5],6))