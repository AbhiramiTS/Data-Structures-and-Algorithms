'''
Reverse an array

i/p: 10, 5, 7, 30
o/p: 30, 7, 5 10

i/p: 30, 20, 5
o/p: 5, 20, 30


'''

# using python reversed method
# def reverse_list(items):
#     return list(reversed(items))

def reverse_list(arr):
    low = 0
    high = len(arr) - 1
    if len(arr) <= 0:
        return
    while low < high:
        temp = arr[low]
        arr[low] = arr[high]
        arr[high] = temp

        low += 1
        high -= 1





def test_reverse_list():
    # Test Case 1: General case
    items1 = [10, 5, 7, 30]
    reverse_list(items1)
    assert items1 == [30, 7, 5, 10]

    # Test Case 2: Another general case
    items2 = [30, 20, 5]
    reverse_list(items2)
    assert items2 == [5, 20, 30]

    # Test Case 3: List with repeated elements
    items3 = [10, 10, 10, 10]
    reverse_list(items3)
    assert items3 == [10, 10, 10, 10]  # Reversed list is the same as the original

    # Test Case 4: List with a single element
    items4 = [42]
    reverse_list(items4)
    assert items4 == [42]  # Reversed list is the same as the original (single element)

    # Test Case 5: Empty list
    items5 = []
    reverse_list(items5)
    assert items5 == []  # Reversed list is the same as the original (empty list)

    print("All test cases passed!")

if __name__ == "__main__":
    items = [10, 5, 7, 30]
    print(items)
    reverse_list(items)
    print(items)

    # Run the test cases
    test_reverse_list()
