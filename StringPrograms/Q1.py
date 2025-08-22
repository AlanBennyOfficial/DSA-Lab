# Write a python script to read an input and display the vowels and consonants in a given string. Display the count of them.
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
