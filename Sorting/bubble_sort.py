def bubble_sort(arr):
    """
    Perform bubble sort on the given array.

    Parameters:
    - arr (list): The input list to be sorted in ascending order.

    Returns:
    None (The input list is sorted in-place).
    """

    # Flag to check if any swaps were made in the inner loop
    swapped = False

    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        # If no swaps were made in the inner loop, the array is already sorted
        if not swapped:
            break



# Test cases
if __name__ == "__main__":
    # Case 1: Random order
    arr1 = [64, 25, 12, 22, 11]
    print("Original array:", arr1)
    bubble_sort(arr1)
    print("Sorted array:", arr1)

    # Case 2: Already sorted
    arr2 = [1, 2, 3, 4, 5]
    print("Original array:", arr2)
    bubble_sort(arr2)
    print("Sorted array:", arr2)

    # Case 3: Descending order
    arr3 = [5, 4, 3, 2, 1]
    print("Original array:", arr3)
    bubble_sort(arr3)
    print("Sorted array:", arr3)
