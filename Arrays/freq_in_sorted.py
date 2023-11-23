'''
Frequencies in a sorted array

i/p: 10, 10, 10, 25, 30, 30
o/p: 10 - 3
     25 - 1
     30 - 2

i/p: 10, 10, 10, 10
o/p: 10 - 4
     
i/p: 10, 20, 30
o/p: 10 - 1
     20 - 1
     30 - 1

'''

def frequency(items):
     dict_items = {}
     if len(items) <= 0:
          return dict_items
     length = 1
     for i in range(1, len(items)):
          if items[i] == items[i - 1]:
               length += 1
          else:
               dict_items[items[i - 1]] = length
               length = 1
     dict_items[items[-1]] = length
     return dict_items





def test_frequency():
    # Test Case 1
    items1 = [10, 10, 10, 25, 30, 30]
    expected_output1 = {10: 3, 25: 1, 30: 2}
    assert frequency(items1) == expected_output1

    # Test Case 2
    items2 = [10, 10, 10, 10]
    expected_output2 = {10: 4}
    assert frequency(items2) == expected_output2

    # Test Case 3
    items3 = [10, 20, 30]
    expected_output3 = {10: 1, 20: 1, 30: 1}
    assert frequency(items3) == expected_output3

    # Test Case 4
    items4 = [5, 5, 5, 5, 5]
    expected_output4 = {5: 5}
    assert frequency(items4) == expected_output4

    # Additional Test Case: Empty list
    items5 = []
    expected_output5 = {}
    assert frequency(items5) == expected_output5

    print("All test cases passed!")

if __name__ == "__main__":
    items = [10, 10, 10, 25, 30, 30, 40]
    print(items)
    res = frequency(items)
    for k, v in res.items():
        print(k, v)

    # Run the test cases
    test_frequency()
