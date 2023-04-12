blue = ["a", "b", "c","d", "e", "f"]

d = dict()
i = 0


while i < len(blue):
   
    if blue[i] > "b":
        d[blue[i]] = "cute"
        i = i+1
    else:
        d[blue[i]] = "batamij"
        i = i+1
print(d)

