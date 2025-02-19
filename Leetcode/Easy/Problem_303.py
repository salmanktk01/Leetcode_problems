#Range Sum Query - Immutable
#what we need to do is to find the range of that specfic sum of that range give in the array. using the array given to you in first index
#["NumArray", "sumRange", "sumRange", "sumRange"] it does not required here 
nums=[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
sum_array=nums[0][0]
result=[None]
for i in range(1,len(sum_array)):
    sum_array[i]=sum_array[i]+sum_array[i-1]
print(sum_array)
for i in range(1,len(nums)):
  left,right=nums[i]
  if(left==0):
     result.append(sum_array[right])
  else:
   result.append(sum_array[right]-sum_array[left-1])
print(result)