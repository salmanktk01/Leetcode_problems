# 2269. Find the K-Beauty of a Number
# Input: num = 430043, k = 2
# Output: 2
# Explanation: The following are the substrings of num of length k:
# - "43" from "430043": 43 is a divisor of 430043.
# - "30" from "430043": 30 is not a divisor of 430043.
# - "00" from "430043": 0 is not a divisor of 430043.
# - "04" from "430043": 4 is not a divisor of 430043.
# - "43" from "430043": 43 is a divisor of 430043.
# Therefore, the k-beauty is 2.
num=430043
k=2
num=str(num)
window_sum=0
for i in range(len(num)-k+1):
     sub_num = int(num[i:i+k])
     if sub_num!=0 and int (num)%sub_num==0 :
          window_sum+=1
print(window_sum)