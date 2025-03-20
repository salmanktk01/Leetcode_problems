# Single Number
# Given a non-empty array of integers nums, every element appears twice except for one

#find that number who is not reapting in array 
#key check : the number comes twice in a array 

nums=[4,2,1,2,1,1]
result=0
for num in nums:
    result^=num
    print(result)
print(nums)