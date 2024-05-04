def subset_combinations_m1(arr):
    res = [[]]
    for i in arr:
        res.extend([j+[i] for j in res])
    return res

def subset_combinations_m2(arr):
    res = [[]]
    for i in arr:
        tmp = []
        for j in res:
            tmp.append(j+[i])
        res.extend(tmp)
    return res

arr = list(map(int,input().split()))
print(f"method 1: {subset_combinations_m1(arr)}")
print(f"method 2: {subset_combinations_m2(arr)}")