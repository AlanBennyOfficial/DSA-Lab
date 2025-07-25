# Given a sentance, count how many times i word appears.

str = "hello world world hello cat rabbit"

dict = {}

for word in str.split():
    if word in dict:
        dict[word] += 1
    else:
        dict[word] = 1

for each in dict:
    print(f"{each} = {dict[each]}")
