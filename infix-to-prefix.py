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
    # Check if the character is a letter (lowercase or uppercase) or a number
    return (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z') or (c >= '0' and c <= '9')

# Function to perform the conversion from infix to prefix
def infix_to_prefix(expression):
    # Reverse the infix expression manually (without using built-in functions)
    expression = list(expression)  # Convert string to list of characters for manual reversal
    expression.reverse()

    stack = []  # Stack to hold operators
    prefix = []  # List to hold the final prefix expression
    prefix_index = 0  # We will manually track the index for prefix list

    for i in range(len(expression)):
        char = expression[i]

        if is_operand(char):  # If the character is an operand (a letter or number)
            prefix.insert(prefix_index, char)  # Insert the operand at the correct position
            prefix_index += 1
        elif char == ')':  # If the character is a closing parenthesis
            stack.append(char)
        elif char == '(':  # If the character is an opening parenthesis
            while stack and stack[-1] != ')':
                prefix.insert(prefix_index, stack.pop())  # Pop from stack until ')' is encountered
                prefix_index += 1
            stack.pop()  # Pop the ')' from the stack
        else:  # If the character is an operator
            while stack and precedence(stack[-1]) > precedence(char):
                prefix.insert(prefix_index, stack.pop())  # Pop operators with higher precedence
                prefix_index += 1
            stack.append(char)  # Push the current operator to the stack

    # Pop all the remaining operators in the stack and insert into prefix
    while stack:
        prefix.insert(prefix_index, stack.pop())
        prefix_index += 1

    # Reverse the prefix expression manually (without using built-in functions)
    prefix.reverse()

    return ''.join(prefix)  # Join the list into a string

# Input expression from the user
infix_expression = input("Enter an infix expression: ")

# Convert the infix expression to prefix
prefix_expression = infix_to_prefix(infix_expression)

# Output the prefix expression
print("Prefix expression:", prefix_expression)
