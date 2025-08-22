str = "Hello World"
dict = {}

for i in str:
    if i in dict.keys():
        dict[i] += 1
    else:
        dict[i] = 1

print(dict)