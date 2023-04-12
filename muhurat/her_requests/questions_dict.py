
#question1
''' Convert two lists into a dictionary
Below are the two lists. Write a Python program to convert them into a dictionary 
in a way that item from list1 is the key and item from list2 is the value'''

aainu = ['Teenie', 'Weenie', 'Tweenie']
bday = [17, 6, 2002]



#question2

''' Merge two Python dictionaries into one
Below are the two dictionaries. Write a Python program to merge them into one dictionary'''

dict1 = {'Teenie': 17, 'Weenie': 6, 'Tweenie': 2002}
dict2 = {'Inu': 28, 'Mam': 10, 'Bebu': 98}

dict3 = dict1.copy()
dict3.update(dict2)
print(dict3)

#question3

'''Print the value of key ‘cuteness’ from the below dict
note: scores are out of 100'''


portfolio = {
    "class": {
        "student": {
            "name": "Aainu",
            "marks": {
                "hotness": 110,
                "cuteness": 120
            }
        }
    }
}


#question4
'''Create a dictionary by extracting the keys from a given dictionary
Write a Python program to create a new dictionary by extracting 
the mentioned keys from the below dictionary.

'''
brewed = {
    "name": "Bebu",
    "goal": "Buddh sa jeewan",
    "age": 20,
    "salary": 8000000,
    "city": "kub's heart"}

#Keys to extract
keys = ["name","goal", "city"]



#question5
'''Delete a list of keys from a dictionary
Write a Python program to remove the mentioned keys from dictionary'''
brewed = {
    "name": "Bebu",
    "goal": "Buddh sa jeewan",
    "age": 20,
    "salary": 8000000,
    "city": "kub's heart"}
# Keys to remove
keys = ["name","goal" "salary"]


#question6

'''Write a Python program to check if value 200 exists in the following dictionary.'''

sample = {'a': 100, 'b': 200, 'c': 300}


#question7
'''Rename key of a dictionary
Write a program to rename a key city to a location in the following dictionary.'''
brewed = {
    "name": "Bebu",
    "goal": "Buddh sa jeewan",
    "age": 20,
    "salary": 8000000,
    "city": "kub's heart"}


#question8
'''Change value of a key in a nested dictionary
Write a Python program to change pari’s salary to 8500 in the following dictionary.'''

saleh = {
    'emp1': {'name': 'charu', 'salary': 7500},
    'emp2': {'name': 'enu', 'salary': 8000},
    'emp3': {'name': 'pari', 'salary': 500}
}


#question9
'''Write a Python program to iterate over dictionaries using for loops.'''
brewed = {
    "name": "Bebu",
    "goal": "Buddh sa jeewan",
    "age": 20,
    "salary": 8000000,
    "city": "kub's heart"}

#question10
'''Print a dictionary where the keys are numbers between 1 and 15 and the values are square of keys'''

#question11
'''Write a Python program to sum all the items in a dictionary.
Write a Python program to multiply all the items in a dictionary.'''
dict1 = {'Teenie': 17, 'Weenie': 6, 'Tweenie': 2002}


baina = [12,23,34,45,12,23,34,45,56,56,34,23,12,2,2,2,2]
d = {}
for i in range(len(baina)):
    if baina[i] not in d:
        d[baina[i]] = 1
        
    else:
        d[baina[i]] = d[baina[i]] + 1

print(d)
l = []
p = max(d.values())
for i in d.keys():
    if d[i]==p:
        print(i)


