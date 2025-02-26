# Move Zeros
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
nums = [0,1,0,3,12]
slow=0
for right in range(len(nums)):
    if(nums[right]!=0 ):
        nums[slow],nums[right]=nums[right],nums[slow]
        slow+=1
print(nums)