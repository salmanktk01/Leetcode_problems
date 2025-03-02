# Given a binary array nums, return the maximum number of consecutive 1's in the array.
# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
#reminder we need to fine the consective 1 in array 
nums = [1, 1, 0, 1, 1, 1]
window_sum = 0
max_sum = 0
left=0
for right in range(len(nums)):
    if(nums[right]==0):
        left=right+1
    else:
        window_sum=right-left+1
        if (max_sum < window_sum):
            max_sum=window_sum
print(max_sum)