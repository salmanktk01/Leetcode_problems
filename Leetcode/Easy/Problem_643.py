#Maximum Average Subarray I
# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
nums = [1,12,-5,-6,50,3]
k = 4

window_sum=sum(nums[:k])
max_sum=window_sum
for i in range(len(nums)-k):
    window_sum=window_sum-nums[i]+nums[i+k] #yeh jao i+k mtlb andar dalo new element as window is changing ,where the nums[i] yeh window se nikal rah hai ,start mein 0 wal opr done 
    if(max_sum  <window_sum):
        max_sum=window_sum
    print(nums[i])
    print(nums[i+k])
    print("/***************/")