#Reverse the Vowels of a String 
# Input: s = "IceCreAm"
# Output: "AceCreIm"
s="IceCream"
vowels=set("aeiouAEIOU")
left,right=0,len(s)-1
s=list(s)
while(left < right):
    while(left < right) and  (s[right] not in vowels) :
        right-=1
    while(left < right) and  (s[left] not in vowels) :
        left+=1
    s[right],s[left]=s[left],s[right]
    right-=1
    left+=1
s="".join(s)
print(s)