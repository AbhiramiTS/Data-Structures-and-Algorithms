
def insertion_sort(arr):
    """
    Perform insertion sort on the given array.

    Parameters:
    - arr (list): The input list to be sorted in ascending order.

    Returns:
    None (The input list is sorted in-place).
    """

    for i in range(1, len(arr)):

        current_element = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > current_element:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = current_element




# Test cases
if __name__ == "__main__":
    # Case 1: Random order
    arr1 = [64, 25, 12, 22, 11]
    print("Original array:", arr1)
    insertion_sort(arr1)
    print("Sorted array:", arr1)

    # Case 2: Already sorted
    arr2 = [1, 2, 3, 4, 5]
    print("Original array:", arr2)
    insertion_sort(arr2)
    print("Sorted array:", arr2)

    # Case 3: Descending order
    arr3 = [5, 4, 3, 2, 1]
    print("Original array:", arr3)
    insertion_sort(arr3)
    print("Sorted array:", arr3)
