# n = int(input("Enter the number of elements: "))

lst = []

for _ in range(5):
    element = int(input("Enter an element: "))
    lst.append(element)

print("First element:", lst[0])
print("Last element:", lst[-1])

print("List of elements:", lst)
print("List of elements in reverse order:", lst[::-1])