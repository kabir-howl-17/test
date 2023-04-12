#stack implementation of valid parenthesis

'''def vp(giva):
    stack = []
    for i in giva:
        if i == "(":
            stack.append(i)
        else:
            if len(stack) == 0:
                return "chutiya hai kya?"
            stack.pop()
    if len(stack) != 0:
        return "invalid"
    else:
        return "valid"

giva = ")((())"
print(vp(giva))'''

s = "abbaca"
stack = []
stack.append(s[0])
for i in range(1,len(s)):
    if len(stack)==0:
        stack.append(s[i])
    elif stack[-1] == s[i]:
        stack.pop()
        
        print(stack)
    else:
        
        stack.append(s[i])
inu = ""
for i in stack:
    inu = inu+i
print(inu)

s = "abbaca"
for i in s:
    if stack and i == stack[-1] :
        stack.pop()
    else:
        stack.append(i)    
        

print(stack)
            