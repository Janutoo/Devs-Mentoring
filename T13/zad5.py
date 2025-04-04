from functools import reduce

nums1 = [1, 2, 3] 
nums2 = [4, 5, 6] 
nums3 = [7, 8, 9] 


total_sum = reduce(lambda acc, x: acc + x, nums1 + nums2 + nums3)
print("Suma trzech list: ", total_sum)