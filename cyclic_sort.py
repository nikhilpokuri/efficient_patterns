def cyclic_sort(nums):
    i = 0
    while i < len(nums):
        correct_index = nums[i] - 1
        if nums[i] != nums[correct_index]:
            print(nums) #swap cyclic until i reaches to it's correct index
            nums[i], nums[correct_index] = nums[correct_index], nums[i]
        else:
            i += 1      
    return nums

nums = [4,3,2,5,1]
print(cyclic_sort(nums)) 
