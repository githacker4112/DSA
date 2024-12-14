def binary_search(arr, target):
    """
    Performs binary search on a sorted array for the target value.

    Parameters:
        arr (list): The sorted list of numbers to search in.
        target (int or float): The number to search for.

    Returns:
        int: Index of the target if found, otherwise -1.
    """
    # Manually determine the length of the array
    n = 0
    for _ in arr:
        n += 1

    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2  # Calculate the middle index
        if arr[mid] == target:
            return mid  # Target found, return index
        elif arr[mid] < target:
            low = mid + 1  # Narrow search to the upper half
        else:
            high = mid - 1  # Narrow search to the lower half

    return -1  # Target not found


# Example usage
if __name__ == "__main__":
    # Sorted array
    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]

    # Number to search for
    target_number = int(input("Enter the number to search for: "))

    # Perform the search
    result = binary_search(numbers, target_number)

    if result != -1:
        print(f"Number found at index {result}.")
    else:
        print("Number not found in the array.")
