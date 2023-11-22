'''
Find the second largest element in the list

i/p: 10, 5, 8, 20
o/p: 0 (Index of 10)

i/p: 20, 10, 20, 8, 12
o/p: 4 (Index of 12)

i/p: 10, 10, 10
o/p: -1 (No second largest elements)

'''

def second_largest(items):
    largest = 0
    sec_index = -1 # Index of the sec largest
    for i in range(1, len(items)):
        if items[i] > items[largest]:
            sec_index = largest
            largest = i
        else:
            if items[i] < items[largest]:
                if sec_index == -1 or items[i] > items[sec_index]:
                    sec_index = i
    return sec_index


def test_second_largest():
    # Test Case 1: General case
    items1 = [10, 5, 8, 20]
    assert second_largest(items1) == 0  # Index of 10

    # Test Case 2: Another general case
    items2 = [20, 10, 20, 8, 12]
    assert second_largest(items2) == 4  # Index of 12

    # Test Case 3: List with all equal elements
    items3 = [10, 10, 10]
    assert second_largest(items3) == -1  # No second largest element

    # Test Case 4: List with repeated elements
    items4 = [1, 2, 2, 3, 3, 3, 4]
    assert second_largest(items4) == 3  # Index of the first occurrence of 3

    # Test Case 5: List with only one element
    items5 = [42]
    assert second_largest(items5) == -1  # No second largest element

    # Test Case 6: Empty list
    items6 = []
    assert second_largest(items6) == -1  # No second largest element

    print("All test cases passed!")

if __name__ == "__main__":
    items = [70, 80, 30, 4, 5, 20, 78]
    sec_largest = second_largest(items)
    print(sec_largest)

    # Run the test cases
    test_second_largest()
