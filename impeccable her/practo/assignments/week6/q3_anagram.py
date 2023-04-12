'''Q - 3 ) Valid Anagram (5 Marks):
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
Example 1:
Input: s = "anagram", t = "nagaram"
Output: true
Example 2:
Input: s = "rat", t = "car"
Output: false'''


s = input("enter a string=  ")
t = input("enter another string=  ")

blue = True
for i in t:
    if i not in s:
        blue = False
        
print(blue)

        


