'''
Find the maximum sum of K consecutive elements


i/p: 1,8,30,-5,20,7
    k = 3
o/p: 45

i/p: 5, -10, 6, 90, 3
    k = 2
o/p: 96

'''


def sliding_window(items, k):
    curr_sum = sum(items[:k])
    max_sum = curr_sum

    for i in range(len(items) - k):
        curr_sum = curr_sum - items[i] + items[k + i]
        max_sum = max(max_sum, curr_sum)

    return max_sum

# Test cases
def test_sliding_window():
    # Test Case 1
    items1 = [1, 8, 30, -5, 20, 7]
    k1 = 3
    assert sliding_window(items1, k1) == 45

    # Test Case 2
    items2 = [5, -10, 6, 90, 3]
    k2 = 2
    assert sliding_window(items2, k2) == 96

    # Additional test cases can be added

    print("All test cases pass")

if __name__ == "__main__":
    test_sliding_window()
