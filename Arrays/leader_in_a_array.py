'''
Leader in a array : A leader is defined as an element for which there are no greater elements to its right.


i/p: 7, 10, 4, 3, 6, 5, 2
o/p: 10, 6, 5, 2 

Explanation:
10 is greater than all the other elements on its right
6 > all the other elements on its right side
5 > all the other elements on its right side
2 > all the other elements on its right side

Hence the leaders are: 10, 6, 5 and 2

i/p: 10, 20, 30
o/p: 30


'''

def find_leader(items):
    leader_list = []
    if len(items) <= 0:
        return leader_list
    leader = items[-1]
    leader_list.append(leader)
    for i in range(len(items) - 2, -1, -1):
        if items[i] > leader:
            leader_list.append(items[i])
            leader = items[i]
    # print(leader_list)
    return leader_list




def test_find_leader():
    # Test Case 1: General case with multiple leaders
    items1 = [7, 10, 2, 4, 3, 6, 5, 2]
    assert find_leader(items1) == [2, 5, 6, 10]  # Leaders are 10, 6, 5, and 2

    # Test Case 2: List with a single element
    items2 = [42]
    assert find_leader(items2) == [42]  # Only one element, which is the leader

    # Test Case 3: List with all elements in ascending order
    items3 = [1, 2, 3, 4, 5]
    assert find_leader(items3) == [5]  # The last element is the leader

    # Test Case 4: List with all elements in descending order
    items4 = [5, 4, 3, 2, 1]
    assert find_leader(items4) == [1, 2, 3, 4, 5]  # All elements are leaders

    # Test Case 5: List with repeated leaders
    items5 = [5, 5, 5, 5, 5]
    assert find_leader(items5) == [5]  # Only the first occurrence of the leader is considered

    # Test Case 6: Empty list
    items6 = []
    assert find_leader(items6) == []  # No leaders in an empty list

    print("All test cases passed!")

if __name__ == "__main__":
    items = [7, 10, 2, 4, 3, 6, 5, 2]
    print(items)
    leaders = find_leader(items)
    print(leaders)

    # Run the test cases
    test_find_leader()
