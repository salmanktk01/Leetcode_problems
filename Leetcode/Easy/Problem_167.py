#Two Sum II - Input Array Is Sorted
#numbers = [2,7,11,15], target = 9
#Output: [1,2]
numbers=[2,7,11,15]
target=9
##SOULTION 1 ,This is not that goood as if we have a bigger list it will take a lot of time 
# slow,fast=0,1
# while(slow<len(numbers)-1):
#     if(numbers[slow]+numbers[fast]==target):
#         print(slow)
#         print(fast)
#         break
#     fast+=1
#     if(fast==len(numbers)):
#         slow+=1
#         fast=slow+1

##SOULTION 2 : The approach we are following is that whenever the number greater than the target then remove the right index and when the number is smaller than the index then we will do left add
n=len(numbers) 
print(n)
left,right=0,n-1
while(left<n-1):
    current_sum=numbers[left]+numbers[right]
    if(current_sum ==target ):
        print(f"{left} and {right}")
    if(current_sum>target):
        right-=1
    else:
        left+=1