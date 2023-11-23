'''
Minimum Consecutive Flips

i/p: 1,1,0,0,0,1
o/p: from 2 to 4

i/p: 1,0,0,0,1,0,0,1,1,1,1
o/p: from 1 to 3
     from 5 to 6

i/p: 1,1,1
o/p:

i/p: 0,1
o/p: from 0 to 0
     from 1 to 1

'''


def min_consecutive_flips(items):

     for i in range(1, len(items)):
          if items[i] != items[i - 1]:
               if items[i] != items[0]:
                    print(f"from index {i}")
               else:
                    print(f"to {i - 1}")

     if items[len(items) - 1] != items[0]:
          print(f"to {len(items) - 1}")
     print("---------------------------------")






def test_min_consecutive_flips():
    # Test Case 1
    items1 = [1, 1, 0, 0, 0, 1]
    min_consecutive_flips(items1)

    # Test Case 2
    items2 = [1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1]
    min_consecutive_flips(items2)

    # Test Case 3
    items3 = [1, 1, 1]
    min_consecutive_flips(items3)

    # Test Case 4
    items4 = [0, 1]
    min_consecutive_flips(items4)

if __name__ == "__main__":
    test_min_consecutive_flips()