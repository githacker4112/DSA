def linear_search_string(string, target):
    """
    Performs a linear search in the string for the target character.

    Parameters:
        string (str): The string to search in.
        target (str): The character to search for.

    Returns:
        int: Index of the target character if found, otherwise -1.
    """
    index = 0  # Initialize the index
    string_length = 0  # Manually calculate the string length

    # Calculate the length of the string
    for _ in string:
        string_length += 1

    # Perform the search
    while index < string_length:
        if string[index] == target:
            return index  # Return the index if target is found
        index += 1  # Move to the next character
    return -1  # Return -1 if the character is not found

# Example usage
if __name__ == "__main__":
    # Input string
    text = input("Enter a string: ")

    # Character to search for
    target_char = input("Enter the character to search for: ")

    # Ensure only a single character is provided
    target_length = 0
    for _ in target_char:
        target_length += 1

    if target_length != 1:
        print("Please enter only one character to search for.")
    else:
        # Perform the search
        result = linear_search_string(text, target_char)

        if result != -1:
            print(f"Character '{target_char}' found at index {result}.")
        else:
            print(f"Character '{target_char}' not found in the string.")
