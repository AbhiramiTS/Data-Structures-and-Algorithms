"""

You are given an array arr[] of N integers. The task is to find the smallest positive number missing from the array.

Note: Positive number starts from 1.

Example 1:

Input:
N = 5
arr[] = {1,2,3,4,5}
Output: 6
Explanation: Smallest positive missing 
number is 6.
Example 2:

Input:
N = 5
arr[] = {0,-10,1,3,-20}
Output: 2
Explanation: Smallest positive missing 
number is 2.
Your Task:
The task is to complete the function missingNumber() which returns the smallest positive missing number in the array.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Constraints:
1 <= N <= 106
-106 <= arr[i] <= 106

 

"""


def missingNumber(self, arr, n):

    arr.sort()

    smallest_positive = 1

    for i in range(n):
        if arr[i] >= 1:
            if arr[i] == smallest_positive:
                smallest_positive += 1
            else:
                # If the current element is greater than the expected smallest positive integer,
                # return the smallest positive integer
                if arr[i] > smallest_positive:
                    return smallest_positive

    # If the array does not contain any missing positive integers,
    # return the next positive integer after the last element in the array
    return arr[n-1] + 1 if arr[n-1] > 0 else 1


result = missingNumber([3, 4, -1, 1], 4)
print(result)  # Output should be 2
