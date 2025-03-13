#First Bad Version
# Input: n = 5, bad = 4
# Output: 4
# Explanation:
# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true
# Then 4 is the first bad version.
n=5
low,high=0,n-1
version=True
while(low < high):
    mid=(low+high)//2
    if badversion(mid):
          high=mid
    else:
         low=mid+1

#logic is correct you just need this badversion thing.
