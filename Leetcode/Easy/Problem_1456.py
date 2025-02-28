#1456. Maximum Number of Vowels in a Substring of Given Length
# Input: s = "abciiidef", k = 3
# Output: 3
# Explanation: The substring "iii" contains 3 vowel letters.
s = "abciiidef"
k = 3
s=list(s)
vowels=set("aeiou")
window_sum=sum(1 for i in range(k) if s[i] in vowels) 
max_sum=window_sum
for i in range(len(s)-k):
        if s[i] in vowels:
                window_sum=window_sum-1
        if s[i+k] in vowels:
                window_sum+=1
        if(window_sum > max_sum):
                max_sum=window_sum
print(max_sum)