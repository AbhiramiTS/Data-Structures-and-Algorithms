'''
Move zeros to end.

i/p: 8, 5, 0, 10, 0, 20
o/p: 8, 5, 10, 20, 0, 0

i/p: 0, 0, 0, 0, 10, 0
o/p: 10, 0, 0, 0, 0, 0

i/p: 10, 20
o/p: 10, 20

'''

def zeros_to_end(arr):
    k = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            temp = arr[i]
            arr[i] = arr[k]
            arr[k] = temp
            k += 1



def test_zeros_to_end():
    # Test Case 1: General case
    items1 = [8, 5, 0, 10, 0, 20]
    zeros_to_end(items1)
    assert items1 == [8, 5, 10, 20, 0, 0]

    # Test Case 2: All zeros at the beginning
    items2 = [0, 0, 0, 0, 10, 0]
    zeros_to_end(items2)
    assert items2 == [10, 0, 0, 0, 0, 0]

    # Test Case 3: No zeros
    items3 = [10, 20]
    zeros_to_end(items3)
    assert items3 == [10, 20]

    # Test Case 4: All zeros
    items4 = [0, 0, 0]
    zeros_to_end(items4)
    assert items4 == [0, 0, 0]

    # Test Case 5: Empty list
    items5 = []
    zeros_to_end(items5)
    assert items5 == []

    print("All test cases passed!")

if __name__ == "__main__":
    items = [8, 5, 0, 10, 0, 20]
    print(items)
    zeros_to_end(items)
    print(items)

    # Run the test cases
    test_zeros_to_end()


