#binary Search 
# Given an array of integers nums which is sorted in ascending order, and an integer target, 
# write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4

#logic work like we need to go to middle of the matrix then if it's greater than rightmost and if lesser than goes towards to the 
#rightmost way.
nums = [0,1,2,4,5,9,5]
target = 9
low,high=0,len(nums)-1
while(low<=high):
    mid=(low+high) //2
    if(nums[mid]==target):
        print(mid)
        break
    elif(nums[mid] > target):
        high=mid-1 #this ignore the left side of the middle
        print(high) 
    else:
      low=mid+1 #this directly ignore the right side of middle 
      print(low)

    
    