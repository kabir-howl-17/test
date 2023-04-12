d = {}
key = []
value = []


for i in range(9):
    n = input("student name = ")
    m = int(input(f"marks of {n}= "))
    d[n] = m
    key.append(n)
    value.append(m)

skey = sorted(key)
svalue = sorted(set(list(value)))
#print(skey)
print(svalue)


output = svalue[1]
result= []
for i in d.keys():
    if d[i] == output:
        result.append(i)

for i in sorted(result):
    print(i)


