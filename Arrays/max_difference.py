'''
Maximum difference problem with order

i/p: 2, 3, 10, 6, 4, 8, 1
o/p: 8

i/p: 7, 9, 5, 6, 3, 2
o/p: 2

i/p: 10, 20, 30
o/p: 20

i/p: 30, 10, 8, 2
o/p: -2

'''

def max_diff(items):
    if items == []:
        return None
    if len(items) == 1:
        return 0
    res = items[1] - items[0]
    min_val = items[0]
    for i in range(1, len(items)):
        res = max(res, items[i] - min_val)
        min_val = min(items[i], min_val)
    return res


def test_max_diff():
    # Test Case 1: General case with positive integers
    items1 = [30, 10, 8, 2]
    assert max_diff(items1) == -2  # Since the array is in decreasing order

    # Test Case 2: General case with positive and negative integers
    items2 = [10, 20, 5, 16, 12]
    assert max_diff(items2) == 11  # Maximum difference is between 5 and 16

    # # Test Case 3: List with all equal elements
    items3 = [7, 7, 7, 7]
    assert max_diff(items3) == 0  # No difference since all elements are equal

    # # Test Case 4: List with one element
    items4 = [42]
    assert max_diff(items4) == 0  # Only one element, so no difference

    # # Test Case 5: Empty list
    items5 = []
    assert max_diff(items5) is None  # No elements in an empty list

    print("All test cases passed!")

if __name__ == "__main__":
    items = [30, 10, 8, 2]
    max_diff(items)

    # Run the test cases
    test_max_diff()
