arr = [10,20,30]
total_sum = sum(arr)
left_sum = 0
# print("left_sum  element  right_sum")
for ele in arr:
    right_sum = total_sum - left_sum - ele
    # print(f"   {left_sum}{' '*6 } {ele}{' '*5 }  {right_sum}")
    print(f"left_sum:{left_sum} [{ele}] right_sum:{right_sum}")
    left_sum += ele