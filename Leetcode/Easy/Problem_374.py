# Guess Number Higher or Lower
# Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.
# You call a pre-defined API int guess(int num), which returns three possible results:
# -1: Your guess is higher than the number I picked (i.e. num > pick).
# 1: Your guess is lower than the number I picked (i.e. num < pick).
# 0: your guess is equal to the number I picked (i.e. num == pick).
# Return the number that I picked.

n = 5
low,high=1,n
while(low < high):
    mid=(low+high)//2
    res=guess(mid)
    if res==0:  #res mean the number is same 
         print(mid)
    if res==1:  #the number is greater 
          high=mid-1
    else:        #the number is lesser
          low=mid+1
