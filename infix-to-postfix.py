# Function to define precedence of operators
def precedence(op):
    if op == '+' or op == '-':
        return 1
    elif op == '*' or op == '/':
        return 2
    elif op == '^':
        return 3
    return 0

# Function to check if a character is an operand (a number or letter)
def is_operand(c):
    # Checks if the character is a letter or number (manual check, no built-in functions)
    return (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z') or (c >= '0' and c <= '9')

# Function to perform the conversion from infix to postfix
def infix_to_postfix(expression):
    stack = []  # Stack to hold operators
    postfix = []  # List to hold the final postfix expression
    
    for char in expression:
        if is_operand(char):  # If the character is an operand (a letter or number)
            postfix.append(char)
        elif char == '(':  # If the character is an opening parenthesis
            stack.append(char)
        elif char == ')':  # If the character is a closing parenthesis
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())  # Pop from stack until '(' is encountered
            stack.pop()  # Pop the '(' from the stack
        else:  # If the character is an operator
            while stack and precedence(stack[-1]) >= precedence(char):
                postfix.append(stack.pop())  # Pop operators with higher or equal precedence
            stack.append(char)  # Push the current operator to the stack

    # Pop all the remaining operators in the stack and append to postfix
    while stack:
        postfix.append(stack.pop())

    return ''.join(postfix)  # Return the postfix expression as a string

# Input expression from the user
infix_expression = input("Enter an infix expression: ")

# Convert the infix expression to postfix
postfix_expression = infix_to_postfix(infix_expression)

# Output the postfix expression
print("Postfix expression:", postfix_expression)
