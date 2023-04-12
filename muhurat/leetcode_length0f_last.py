strr = "i am very sad  "
print(len(strr))
aainu = ""
for i in strr:
    if i == " ":
        strr.remove(i)
    else:
        aainu = strr
        break


print(aainu)
print(len(aainu))