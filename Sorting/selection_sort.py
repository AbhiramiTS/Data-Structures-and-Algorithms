def selection_sort(arr):
    """
    Perform selection sort on the given array.

    Parameters:
    - arr (list): The input list to be sorted in ascending order.

    Returns:
    None (The input list is sorted in-place).
    """

    for i in range(len(arr)):

        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]




# Test cases
if __name__ == "__main__":
    # Case 1: Random order
    arr1 = [64, 25, 12, 22, 11]
    print("Original array:", arr1)
    selection_sort(arr1)
    print("Sorted array:", arr1)

    # Case 2: Already sorted
    arr2 = [1, 2, 3, 4, 5]
    print("Original array:", arr2)
    selection_sort(arr2)
    print("Sorted array:", arr2)

    # Case 3: Descending order
    arr3 = [5, 4, 3, 2, 1]
    print("Original array:", arr3)
    selection_sort(arr3)
    print("Sorted array:", arr3)
