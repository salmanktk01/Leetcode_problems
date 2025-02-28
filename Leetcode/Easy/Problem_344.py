#reverse the string 
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
s = ["h","e","l","l","o"]
left,right=0,len(s)-1
while(left<right):
   s[left],s[right]=s[right],s[left]
   right-=1
   left+=1
print(s)
