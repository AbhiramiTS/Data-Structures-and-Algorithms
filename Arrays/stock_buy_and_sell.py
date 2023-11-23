'''
Stock Buy and Sell Problem

i/p: 1,5,3,8,12
o/p: 13

i/p: 30, 20, 10
o/p: 0

i/p: 10, 20, 30
o/p: 20

i/p: 1,5,3,1,2,8
o/p: 11

'''

def max_profit(items):
    profit = 0
    for i in range(1, len(items)):
        if items[i] > items[i - 1]:
            profit += (items[i] - items[i - 1])

    return profit


def test_max_profit():
    # Test Case 1
    items = [1, 5, 3, 8, 12]
    assert max_profit(items) == 13

    # Test Case 2
    items = [30, 20, 10]
    assert max_profit(items) == 0

    # Test Case 3
    items = [10, 20, 30]
    assert max_profit(items) == 20

    # Test Case 4
    items = [1, 5, 3, 1, 2, 8]
    assert max_profit(items) == 11

    # Test Case 5
    items = [3, 2, 6, 8, 4, 10, 5, 12]
    assert max_profit(items) == 19

    # # Test Case 6
    items = [5, 4, 3, 2, 1]
    assert max_profit(items) == 0

    print("All test cases pass")



if __name__ == "__main__":
    items = [3, 2, 6, 8, 4, 10, 5, 12]
    print(items)
    profit = max_profit(items)
    print(profit)
    test_max_profit()


