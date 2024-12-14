def bubble_sort_strings(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# Example usage
if __name__ == "__main__":
    # Sample array of strings
    arr = ["banana", "apple", "cherry", "date", "fig", "grape", "kiwi"]
    print("Original array:", arr)
    
    sorted_arr = bubble_sort_strings(arr)
    print("Sorted array:", sorted_arr)
