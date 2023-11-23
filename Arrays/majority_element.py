'''
Majority Element

i/p: 8,3,4,8,8
o/p: 0 or 3 or 4 (Any index of 8)

i/p: 3,7,4,7,7,5
o/p: -1 (No majority)

i/p: 20,30,40,50,50,50,50
o/p: 3 or 4 or 5 or 6 (Any index of 50)

'''

def is_majority_element(items, res):

    majority_count = 0
    for i in range(len(items)):
        if items[res] == items[i]:
            majority_count += 1
    if majority_count <= len(items)//2:
        return False
    return True


def find_majority_element(items):

    count = 1
    res = 0
    for i in range(1, len(items)):
        if items[i] == items[i - 1]:
            count += 1
        else:
            count -= 1
            if count == 0:
                count = 1
                res = i
    
    is_majority = is_majority_element(items, res)
    return res if is_majority else False


# Test cases
def test_find_majority_element():
    # Test Case 1
    items1 = [8, 3, 4, 8, 8]
    assert find_majority_element(items1) in [0, 3, 4]

    # Test Case 2
    items2 = [3, 7, 4, 7, 7, 5]
    assert find_majority_element(items2) is False

    # Test Case 3
    items3 = [20, 30, 40, 50, 50, 50, 50]
    assert find_majority_element(items3) in [3, 4, 5, 6]

    print("All test cases pass")

if __name__ == "__main__":
    test_find_majority_element()



    
    




