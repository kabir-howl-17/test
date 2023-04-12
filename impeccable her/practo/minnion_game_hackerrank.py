string = input("give a word input for minion game = ")
decider = len(string)
vowels = 0
consonants = 0
     
for i in range(decider):
    if string[i] in "AEIOUaeiou":
           vowels = vowels+(decider-i)
    else:
        consonants = consonants+(decider-i)
                
if vowels < consonants:
    print("Stuart" + str(consonants))
elif vowels > consonants:
    print("Kevin" + str(vowels))
else:
    print("Draw")