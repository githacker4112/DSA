# Function to evaluate postfix expression
def evaluate_postfix(expression):
    stack = []

    # Loop through each character in the postfix expression
    for char in expression:
        # If the character is an operand (number), push it to the stack
        if char.isdigit():
            stack.append(int(char))
        
        # If the character is an operator
        elif char in '+-*/^':
            # Pop two operands from the stack
            operand2 = stack.pop()
            operand1 = stack.pop()
            
            # Perform the operation based on the operator
            if char == '+':
                result = operand1 + operand2
            elif char == '-':
                result = operand1 - operand2
            elif char == '*':
                result = operand1 * operand2
            elif char == '/':
                result = operand1 / operand2
            elif char == '^':
                result = operand1 ** operand2
            
            # Push the result of the operation back to the stack
            stack.append(result)
    
    # The final result will be the only item left in the stack
    return stack[-1]

# Input postfix expression from the user
postfix_expression = input("Enter a postfix expression: ")

# Evaluate the postfix expression
result = evaluate_postfix(postfix_expression)

# Output the result
print("Result of the postfix expression:", result)
