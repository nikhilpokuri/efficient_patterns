arr = [10, 20, 30, 40, 50]
prefix_sum = [10]
for i in range(1, len(arr)):
    prev = prefix_sum[-1]
    prefix_sum.append(prev + arr[i])
print(prefix_sum)

"""
#Example
arr = [10,20,30]
total_sum = sum(arr)
left_sum = 0

#To find the right_sum and left_sum of element at a time
for ele in arr:
    right_sum = total_sum - left_sum - ele
    print(f"left_sum:{left_sum} [{ele}] right_sum:{right_sum}")
    left_sum += ele

"""