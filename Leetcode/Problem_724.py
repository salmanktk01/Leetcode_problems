#Find Pivot Index 
#The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

nums = [1,7,3,6,5,6]
n=len(nums)
prefix_right=[0]*(n)
prefix_left=[0]*(n)
prefix_right[0]=nums[0]
prefix_left[0]=nums[0]
for i in range(1,n):
    if(prefix_right[i]==prefix_left[i]):
          print(i)
    prefix_left[i]=prefix_left[i-1]+nums[i]
    prefix_right[i]=prefix_right[i-1]+nums[i-n]
print("not possible")