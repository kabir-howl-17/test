'''n = int(input("n here = "))
student_marks = {}
for _ in range(n):
    name, *line = input("add please = ").split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input("name of student=  ")
print(name)
print(scores)'''

d = {"alpha": [23,34,56],"beta": [45,56,67], "gama": [35,67,78]}

for i in d:
    res = d[i]

print(type(res))


'''res = {}
les = []
    for i in student_marks:
        les = student_marks[i]
        bud = sum(les)/len(les)
        res[i] = "%.2f"%bud
        if query_name == i:
            print(res[i])'''
