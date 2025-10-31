from collections import deque

def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '%': 2, '^': 3}
    
    stack = []          # Operators
    output = deque()    # Output
    
    for char in expression:
        if char.isalnum():  # If character is operand (letter or number)
            output.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()     # Remove '('
        else:
            while (stack and stack[-1] != '(' and 
                   precedence.get(char, 0) <= precedence.get(stack[-1], 0)):
                output.append(stack.pop())
            stack.append(char)
    
    # Pop remaining operators from stack
    while stack:
        output.append(stack.pop())
    
    return ''.join(output)


expression = "A+B*(C-D)"
result = infix_to_postfix(expression)
print(f"Infix: {expression}")
print(f"Postfix: {result}")