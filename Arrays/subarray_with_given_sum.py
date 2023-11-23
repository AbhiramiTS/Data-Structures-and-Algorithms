'''
Subarray with given sum (There are no negative elements in the array)

i/p: 1,4,20,3,10,5
    sum = 33
o/p: YES

i/p: 1,4,0,0,3,10,5
    sum = 7
o/p: YES

i/p: 2,4
    sum = 3
o/p: NO

'''


def find_subarray(items, num):
    index = 0
    curr_sum = 0

    for i in range(len(items)):
        curr_sum += items[i]

        while curr_sum > num:
            curr_sum -= items[index]
            index += 1

        if curr_sum == num:
            return "YES"

    return "NO"

# Test cases
def test_find_subarray():
    # Test Case 1
    items1 = [1, 4, 20, 3, 10, 5]
    sum1 = 33
    assert find_subarray(items1, sum1) == "YES"

    # Test Case 2
    items2 = [1, 4, 0, 0, 3, 10, 5]
    sum2 = 7
    assert find_subarray(items2, sum2) == "YES"

    # Test Case 3
    items3 = [2, 4]
    sum3 = 3
    assert find_subarray(items3, sum3) == "NO"

    # Additional test cases can be added

    print("All test cases pass")

if __name__ == "__main__":
    test_find_subarray()

