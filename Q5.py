lst = [1,1,2,2,2,3,4,5]

st = set(lst)

for i in st:
    print(f"Occurances of {i}: ",lst.count(i))

print("Unique list: ",st)