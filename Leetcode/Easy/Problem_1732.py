# Input: gain = [-5,1,5,0,-7]
# Output: 1
#what we do is to sum the previous value and get new array 
gain = [-4,-3,-2,-1,4,3,2]
n=len(gain)+1
gain.insert(0,0)
print(gain)
for i in range(1,n):
    gain[i]=gain[i-1]+gain[i]
print(max(gain))
print(gain)
