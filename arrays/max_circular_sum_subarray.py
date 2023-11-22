'''
Maximum Circular sum subarray



'''

def min_subarray_sum(items):

    max_sum = [0] * len(items)
    max_sum[0] = items[0]
    res = items[0]
    for i in range(1, len(items)):
        max_sum[i] = min(max_sum[i - 1] + items[i], items[i])
        res = min(res, max_sum[i])

    return res

def max_circular_sum(items):
    return sum(items) - min_subarray_sum(items)



def test_max_circular_sum():
    # Test Case 1
    items1 = [1, -2, 3, -2]
    assert max_circular_sum(items1) == 3

    # Test Case 2
    items2 = [5, -3, 5]
    assert max_circular_sum(items2) == 10

    # Test Case 3
    items3 = [3, -1, 2, -1]
    assert max_circular_sum(items3) == 4

    # Test Case 4
    items4 = [3, -2, 2, -3]
    assert max_circular_sum(items4) == 3

    # Test Case 5
    items5 = [-2, -3, -1]
    assert max_circular_sum(items5) == -1

    print("All test cases pass")

if __name__ == "__main__":
    test_max_circular_sum()

    