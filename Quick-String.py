def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

# Example usage
if __name__ == "__main__":
    # Sample array of strings
    arr = ["banana", "apple", "cherry", "date", "fig", "grape", "kiwi"]
    print("Original array:", arr)
    
    sorted_arr = quick_sort(arr)
    print("Sorted array:", sorted_arr)
