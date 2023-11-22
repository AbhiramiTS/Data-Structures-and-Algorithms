'''
Check if an array is sorted

i/p: 8, 12, 15
o/p: YES

i/p: 8, 10, 10, 12
o/p: YES

i/p: 100
o/p: YES

i/p: 200, 100, 50
o/p: NO (Checks for only increasing order) 

i/p: 100, 20, 200
o/p: NO

'''

# Using Python sorted method
# def is_sorted(list_items):
#     return sorted(list_items) == list_items
        # or
    # return all(list_items[i] <= list_items[i+1] for i in range(len(list_items) - 1))



def is_sorted(arr):

    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            return False
    return True




def test_is_sorted():
    # Test Case 1: Unsorted list
    items1 = [70, 80, 30, 4, 5, 20, 78]
    assert not is_sorted(items1)

    # Test Case 2: Sorted list
    items2 = [1, 2, 40, 50, 67, 89, 90]
    assert is_sorted(items2)

    # Test Case 3: Empty list
    items3 = []
    assert is_sorted(items3)

    # Test Case 4: Single-element list
    items4 = [42]
    assert is_sorted(items4)

    # Test Case 5: Repeated elements
    items5 = [10, 10, 10, 10]
    assert is_sorted(items5)

    print("All test cases passed!")

if __name__ == "__main__":
    # Uncomment the line below to test a different set of items
    # items = [70, 80, 30, 4, 5, 20, 78] 
    items = [1, 2, 40, 50, 67, 89, 90]
    res = is_sorted(items)
    print(res)

    # Run the test cases
    test_is_sorted()
