str = "Hello, World"

UpperCase = 0
LowerCase = 0
Digit = 0
notalnum = 0

for i in str:
    if i.isupper():
        UpperCase+=1
    elif i.islower():
        LowerCase+=1
    elif i.isdigit():
        Digit+=1
    elif not i.isalpha() and not i.isspace():
        notalnum+=1
    

print(f"Uppercase: {UpperCase}\nLowercase: {LowerCase}\nDigit: {Digit}\nSpecial Character: {notalnum}")
