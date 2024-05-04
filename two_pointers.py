arr = sorted(list(map(int,input("Enter arr Elements: ").split())))
target = int(input("Enter Target Sum: "))

def target_sum(arr, target):
#check if there is any pair sum that matches target
    start = 0
    end = len(arr)-1

    res_pairs = []
    while start < end:
        curr = arr[start] + arr[end]
        if curr > target:
            end -= 1
        elif curr < target:
            start += 1
        else:
            res_pairs.append([arr[start], arr[end]])
            start += 1
    if not res_pairs:
        return 'No Pair sum equals to target'
    else:
        return res_pairs
print(target_sum(arr, target))