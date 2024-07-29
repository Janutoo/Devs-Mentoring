nums = [4, 6, 8, 24, 12, 2]
cos = 0 
cos2 = 0 
for key,value in enumerate(nums):
    if cos < value:
        cos = value
        cos2 = key
print(cos2)
print(cos)
   