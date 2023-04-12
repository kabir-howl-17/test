'''write a code that takes string of integers spearated by space and return a list of integers'''

#q1
n = input("a string of numbers separated by space = ")

intlist = n.split()
mint = len(intlist)
brew = []
print(int(n[0]))
for i in range(mint):
    hint = int(intlist[i])
    brew.append(hint)
print(intlist)
print(brew)




