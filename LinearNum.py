def linear_search(arr, target):
   
    index = 0  
    while index < len(arr):
        if arr[index] == target:
            return index  
        index += 1  
    return -1  
if __name__ == "__main__":
   
    numbers = [12, 34, 56, 78, 90, 23, 45]

    target_number = int(input("Enter the number to search for: "))

   
    result = linear_search(numbers, target_number)

    if result != -1:
        print(f"Number found at index {result}.")
    else:
        print("Number not found in the array.")
