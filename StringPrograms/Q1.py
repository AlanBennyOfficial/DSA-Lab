str = input("Enter a string:")
vowels = 0 
consonants = 0

for i in str:
    if i in "aeiou":
        vowels+=1
    elif i in "bcdfghjklmnpqrstvwxyz":
        consonants+=1

print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")