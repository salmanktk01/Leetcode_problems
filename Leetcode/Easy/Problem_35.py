#  Search Insert Position
# Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2
#rember you need to find the number where it will relay if it is not present 
nums=[1,3,5,6]
target=2
low,high=0,len(nums)-1
while(low<=high):
    mid=(low+high)//2
    if(nums[mid]==target): #if the target is present then it will print this 
        print(mid)
        break
    if(nums[mid] > target):
         high=mid-1
    else:
        low=mid+1
print(low) #when the target is not present in the array