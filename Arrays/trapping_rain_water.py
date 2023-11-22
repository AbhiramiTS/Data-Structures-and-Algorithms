'''
Trapping Rain Water

i/p: [2, 0, 2]
o/p: 2

i/p: [3, 0, 1, 2, 5]
o/p: 6

'''

def trapping_water(items):

    lmax = items[0]
    lmax_list= []
    lmax_list.append(lmax)
    for i in range(1, len(items)):
        lmax = max(items[i],lmax)
        lmax_list.append(lmax)

    rmax = items[-1]
    rmax_list = []
    rmax_list.append(items[-1])
    for i in range(len(items) - 2, -1, -1):
        rmax = max(items[i],rmax)
        rmax_list.append(rmax)
    rmax_list.reverse()

    res = 0
    for i in range(len(items)):
        res += (min(lmax_list[i], rmax_list[i]) - items[i])
    return res


def test_trapping_water():
    # Test Case 1
    items = [2, 0, 2]
    assert trapping_water(items) == 2

    # # Test Case 2
    items = [3, 0, 1, 2, 5]
    assert trapping_water(items) == 6

    # Test Case 3
    items = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    assert trapping_water(items) == 6

    # # Test Case 4
    items = [4, 2, 0, 3, 2, 5]
    assert trapping_water(items) == 9

    # # Test Case 5
    items = [1, 2, 3, 4, 5]
    assert trapping_water(items) == 0

    # # Test Case 6
    items = [5, 4, 3, 2, 1]
    assert trapping_water(items) == 0

    print("All test cases pass")

if __name__ == "__main__":
    test_trapping_water()

