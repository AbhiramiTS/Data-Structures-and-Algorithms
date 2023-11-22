'''
Find the index of largest element in the array

i/p: 10, 5, 20, 8
o/p: 2

'''



def find_largest(item_list):
    if len(item_list) <= 0:
        return None
    return item_list.index((max(item_list)))



def test_find_largest():
    # Test Case 1: List with positive integers
    items1 = [10, 5, 20, 8]
    assert find_largest(items1) == 2  # Index of the largest element (20)

    # Test Case 2: List with negative integers
    items2 = [-5, -10, -3, -8]
    assert find_largest(items2) == 2  # Index of the largest element (-3)

    # Test Case 3: List with positive and negative integers
    items3 = [5, -10, 20, -8]
    assert find_largest(items3) == 2  # Index of the largest element (20)

    # Test Case 4: List with repeated largest elements
    items4 = [10, 20, 20, 8, 20]
    assert find_largest(items4) == 1  # Index of the first occurrence of the largest element (20)

    # Test Case 5: Empty list
    items5 = []
    assert find_largest(items5) is None  # No largest element in an empty list

    # Test Case 6: List with a single element
    items6 = [42]
    assert find_largest(items6) == 0  # Index of the only element in the list

    print("All test cases passed!")

if __name__ == "__main__":
    items = [10, 5, 20, 8]
    largest = find_largest(items)
    print(largest)

    # Run the test cases
    test_find_largest()
