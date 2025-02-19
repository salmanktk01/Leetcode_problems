#Running Sum of 1d Array 
#output: [1,3,6,10]
nums = [1,2,3,4]
n=len(nums)
prefix_sum = [0] * (n) 
prefix_sum[0] = nums[0]
for i in range(1,n): 
    print(i) 
    prefix_sum[i]=prefix_sum[i-1]+nums[i]
print(prefix_sum)