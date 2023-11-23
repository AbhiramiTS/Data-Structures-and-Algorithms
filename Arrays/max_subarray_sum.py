'''
Maximum Subarray

i/p: 2,3,-8,7,-1,2,3
o/p: 11

i/p: 5,8,3
o/p: 16


'''

def max_subarray_sum(items):

    max_sum = [0] * len(items)
    max_sum[0] = items[0]
    res = items[0]
    for i in range(1, len(items)):
        max_sum[i] = max(max_sum[i - 1] + items[i], items[i])
        res = max(res, max_sum[i])

    return res

# Test cases
def test_max_subarray_sum():
    # Test Case 1
    items1 = [2, 3, -8, 7, -1, 2, 3]
    assert max_subarray_sum(items1) == 11

    # Test Case 2
    items2 = [5, 8, 3]
    assert max_subarray_sum(items2) == 16

    # # # Test Case 3
    items3 = [1, 2, 3, 4, 5]
    assert max_subarray_sum(items3) == 15

    # # # Test Case 4
    items4 = [-2, -5, 6, -2, -3, 1, 5, -6]
    assert max_subarray_sum(items4) == 7

    print("All test cases pass")

if __name__ == "__main__":
    test_max_subarray_sum()