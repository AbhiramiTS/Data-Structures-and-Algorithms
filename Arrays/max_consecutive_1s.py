'''
Maximum consecutive 1s in a Binary array.

i/p: 0,1,1,0,1,0
o/p: 2

i/p: 1,1,1,1
o/p: 4

i/p: 0,0,0
o/p: 0

i/p: 1,0,1,1,1,1,0,1,1
o/p: 4

'''

def max_consecutive(items):
    count = 0
    res = 0
    for i in range(len(items)):
        if items[i] == 1:
            count += 1
            res = max(count, res)
        else:
            count = 0

    return res


def test_max_consecutive():
    # Test Case 1
    items = [0, 1, 1, 0, 1, 0]
    assert max_consecutive(items) == 2

    # Test Case 2
    items = [1, 1, 1, 1]
    assert max_consecutive(items) == 4

    # Test Case 3
    items = [0, 0, 0]
    assert max_consecutive(items) == 0

    # Test Case 4
    items = [1, 0, 1, 1, 1, 1, 0, 1, 1]
    assert max_consecutive(items) == 4

    # Test Case 5
    items = [1, 0, 1, 0, 1, 0, 1]
    assert max_consecutive(items) == 1

    # Test Case 6
    items = [1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1]
    assert max_consecutive(items) == 5

    print("All test cases pass")

if __name__ == "__main__":
    test_max_consecutive()
