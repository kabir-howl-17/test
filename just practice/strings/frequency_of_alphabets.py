




str = "google.com"
dict = {}
for i in str:
    keys = dict.keys()
    #print(keys)
    #print(dict)
    if i in keys:
        dict[i] =  dict[i]+1
    else:
        dict[i] = 1
print(dict)
