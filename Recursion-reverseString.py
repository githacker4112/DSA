def reverse_string(s):
    # Base case: if the string is empty or has only one character
    if len(s) == 0:
        return s
    else:
        # Recursive case: reverse the substring excluding the first character
        # and append the first character at the end
        return reverse_string(s[1:]) + s[0]

# Input string from the user
input_string = input("Enter a string: ")

# Call the function and print the reversed string
reversed_string = reverse_string(input_string)
print(f"Reversed string: {reversed_string}")
