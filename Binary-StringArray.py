def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        mid_val = arr[mid]
        
        if mid_val == target:
            return mid
        elif mid_val < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1  # Return -1 if the target is not found

# Example usage
arr = ["apple", "banana", "cherry", "date", "fig", "grape", "kiwi"]
target = "fig"

# Ensure the array is sorted before performing binary search
arr.sort()
result = binary_search(arr, target)

if result != -1:
    print(f"'{target}' found at index {result}.")
else:
    print(f"'{target}' not found in the array.")
