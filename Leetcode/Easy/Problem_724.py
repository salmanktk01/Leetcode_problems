#Find Pivot Index 
#The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

nums = [-1,-1,-1,-1,-1,0]
n=len(nums)
total_sum=sum(nums)
left_sum,right_sum=0,0
for i in range(n):
    right_sum=total_sum-left_sum-nums[i] #nums[i] asae lie cause woe left_sum baad mein add ho rah hai na 
    if(left_sum==right_sum):
        print(i)
        break
    left_sum+=nums[i]
print("not posb")