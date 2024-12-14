def max_heapify(arr, n, i):
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # left child index
    right = 2 * i + 2  # right child index

    # Check if left child exists and is greater than root
    if left < n and arr[i] < arr[left]:
        largest = left

    # Check if right child exists and is greater than largest so far
    if right < n and arr[largest] < arr[right]:
        largest = right

    # Change root if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root
        max_heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Build a maxheap
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        max_heapify(arr, i, 0)

    return arr

# Example usage
if __name__ == "__main__":
    # Sample array
    arr = [12, 11, 13, 5, 6, 7]
    print("Original array:", arr)

    sorted_arr = heap_sort(arr)
    print("Sorted array:", sorted_arr)
