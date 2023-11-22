'''
Left rotate an array by d places

i/p: 1,2,3,4,5
o/p: 2,3,4,5,1

i/p: 30, 5, 20
o/p: 5, 20, 30

'''

# TODO

def validate_and_adjust_d(d, size):
    if size == 0:
        return 0
    d = d % size
    while d > size:
        d = d % size
    return d

def left_rotate(list_items, size, d):
    d = validate_and_adjust_d(d, size)
    reverse(list_items, 0, d - 1)
    reverse(list_items, d, size - 1)
    reverse(list_items, 0, size - 1)


def right_rotate(list_items, size, d):
    d = validate_and_adjust_d(d, size)
    reverse(list_items, 0, size - 1)
    reverse(list_items, 0, d - 1)
    reverse(list_items, d, size - 1)

def reverse(list_items, low, high):

    while low < high:
        temp = list_items[low]
        list_items[low] = list_items[high]
        list_items[high] = temp

        low += 1
        high -= 1
    # print(list_items)




def test_rotate():
    # Test Case 1: Left rotate by 2 positions
    items1 = [1, 2, 3, 4, 5]
    left_rotate(items1, len(items1), 2)
    assert items1 == [3, 4, 5, 1, 2]

    # Test Case 2: Right rotate by 2 positions
    items2 = [1, 2, 3, 4, 5]
    right_rotate(items2, len(items2), 2)
    assert items2 == [4, 5, 1, 2, 3]

    # Test Case 3: Left rotate by the size of the list (no change)
    items3 = [10, 20, 30]
    left_rotate(items3, len(items3), len(items3))
    assert items3 == [10, 20, 30]

    # Test Case 4: Right rotate by more than the size of the list
    items4 = [1, 2, 3, 4, 5]
    right_rotate(items4, len(items4), 7)
    assert items4 == [4, 5, 1, 2, 3]  # Equivalent to rotating by 2 positions

    # Test Case 5: Left rotate an empty list (no change)
    items5 = []
    left_rotate(items5, 0, 3)
    assert items5 == []

    # Test Case 6: Right rotate an empty list (no change)
    items6 = []
    right_rotate(items6, 0, 3)
    assert items6 == []

    # Test Case 7: Left rotate by 0 positions (no change)
    items7 = [1, 2, 3, 4, 5]
    left_rotate(items7, len(items7), 0)
    assert items7 == [1, 2, 3, 4, 5]

    # Test Case 8: Right rotate by 0 positions (no change)
    items8 = [1, 2, 3, 4, 5]
    right_rotate(items8, len(items8), 0)
    assert items8 == [1, 2, 3, 4, 5]

    print("All test cases passed!")

if __name__ == "__main__":
    left_items = [1, 2, 3, 4, 5]
    d = 2  # Replace with user input or another method to get the value of d
    left_rotate(left_items, len(left_items), d)
    # print("Left Rotate : ", left_items)
    items = [1, 2, 3, 4, 5]
    right_rotate(items, len(items), d)
    # print("Right Rotate : ", items)
    # Run the test cases
    test_rotate()

