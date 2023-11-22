'''
Remove duplicates from a sorted array

i/p: 10, 20, 20, 30, 30, 30, 30; size = 7
o/p: 10, 20, 30; size = 3

i/p: 10, 10, 10; size = 3
o/p: 10; size = 1


'''


# Using python set
# def remove_duplicates(items):
#     return set(items)

def remove_duplicates(arr):
    if arr == []:
        return 0
    res = 1
    if len(arr) == 1:
        return res
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            arr[res] = arr[i]
            res += 1
    return res



def test_remove_duplicates():
    # Test Case 1: General case with duplicates
    items1 = [10, 10, 20, 20, 20, 30, 30, 30, 30]
    res1 = remove_duplicates(items1)
    assert items1[:res1] == [10, 20, 30]  # After removing duplicates
    assert res1 == 3  # New size of the array

    # Test Case 2: All elements are the same
    items2 = [10, 10, 10]
    res2 = remove_duplicates(items2)
    assert items2[:res2] == [10]  # After removing duplicates
    assert res2 == 1  # New size of the array

    # Test Case 3: No duplicates
    items3 = [1, 2, 3, 4, 5]
    res3 = remove_duplicates(items3)
    assert items3[:res3] == [1, 2, 3, 4, 5]  # No duplicates, array remains the same
    assert res3 == 5  # Size remains the same

    # Test Case 4: Empty array
    items4 = []
    res4 = remove_duplicates(items4)
    assert items4[:res4] == []  # No duplicates in an empty array
    assert res4 == 0  # Size remains 0

    print("All test cases passed!")

if __name__ == "__main__":
    items = [10, 10, 20, 20, 20, 30, 30, 30, 30]
    print(items)
    res = remove_duplicates(items)
    print(items[:res])

    # Run the test cases
    test_remove_duplicates()
