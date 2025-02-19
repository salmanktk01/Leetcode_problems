#Subarray Sum Equals K 
#Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
#this mean how many subarray think can made that specific thing 
#contniougs hai means start se add krna pry gy asae 
#sliding window when we be asked to give us less,greater type thing 
#Input: nums = [1,1,1], k = 2
#Output: 2
nums=[1,-1,0]
nums.insert(0,0)
k=0
n=len(nums)
count=0
for i in range(1,n):
    if(nums[i]==k or nums[i]+nums[i-1]==k):
        count+=1
    elif(nums[i]+nums[i-1]<k):
        if(nums[i]+nums[i-1]+nums[i-2]==k):
            count+=1
print(count)
print(nums)