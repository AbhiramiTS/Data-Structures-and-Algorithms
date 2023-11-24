'''
Minimum adjacent difference in a circular array

Given an array Arr of n integers arranged in a circular fashion. Your task is to find the minimum absolute difference between adjacent elements.

Example 1:

Input:
n = 7
Arr[] = {8,-8,9,-9,10,-11,12}
Output: 4
Explanation: The absolute difference 
between adjacent elements in the given 
array are as such: 16 17 18  19 21 23 4
(first and last). Among the calculated 
absolute difference the minimum is 4.
Example 2:

Input:
n = 8
Arr[] = {10,-3,-4,7,6,5,-4,-1}
Output: 1
Explanation: The absolute difference 
between adjacent elements in the given 
array are as such: 13 1 11 1 1 9 3 11
(first and last).  Among the calculated 
absolute difference, the minimum is 1.
Your Task:
The task is to complete the function minAdjDiff() which returns the minimum difference between adjacent elements in circular array.

Expected Time Complexity: O(n).
Expected Auxiliary Space: O(1).

Constraint:
2 <= n <= 106
-106 <= Arr[i] <= 106

'''

def minAdjDiff(arr, n):
        
    min_difference = abs(arr[0] - arr[1])
    for i in range(1, n):
        
        min_difference = min(min_difference, abs(arr[i % n] - arr[(i+1) % n]))

    return min_difference


n1 = 7
arr1 = [8, -8, 9, -9, 10, -11, 12]
print(minAdjDiff(arr1, n1))  # Output: 4

n2 = 8
arr2 = [10, -3, -4, 7, 6, 5, -4, -1]
print(minAdjDiff(arr2, n2))  # Output: 1