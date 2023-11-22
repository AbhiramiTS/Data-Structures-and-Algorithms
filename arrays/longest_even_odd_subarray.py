'''
Longest Even Odd Subarray

i/p: 10, 12, 14, 7, 8
o/p: 3

i/p: 7, 10, 13, 14
o/p: 4

i/p: 10, 12, 8, 4
o/p: 1

'''

def longest_even_odd(items):

    res = 1
    count = 1
    for i in range(1, len(items)):
        if (items[i]%2 == 0 and items[i-1]%2 != 0) or (items[i]%2 != 0 and items[i-1]%2 == 0):
            count += 1
            res = max(res, count)
        else:
            count = 1

    return res



# Test cases
def test_longest_even_odd():
    # Test Case 1
    items1 = [10, 12, 14, 7, 8]
    assert longest_even_odd(items1) == 3

    # # # Test Case 2
    items2 = [7, 10, 13, 14]
    assert longest_even_odd(items2) == 4

    # # Test Case 3
    items3 = [10, 12, 8, 4]
    assert longest_even_odd(items3) == 1

    # # Test Case 4
    items4 = [2, 4, 6, 8, 10]
    assert longest_even_odd(items4) == 1

    print("All test cases pass")

if __name__ == "__main__":
    test_longest_even_odd()