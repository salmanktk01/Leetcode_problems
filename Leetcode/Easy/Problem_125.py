# Valid Palindrome
#Input: s = "A man, a plan, a canal: Panama"
# Output: true
s = "A man, a plan, a canal: Panama"
s=s.lower()
strs=[char for char in s if  char.isalnum()]
left,right=0,len(strs)-1
print(right)
print(strs[left])
print(strs[right])
pal=False
while(left-1!=right+1):
    if(strs[left]==strs[right]):
        pal=True
        left+=1
        right-=1
print(pal)