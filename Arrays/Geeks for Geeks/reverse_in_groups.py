'''
Given an array arr[] of positive integers of size N. Reverse every sub-array group of size K.

Note: If at any instance, there are no more subarrays of size greater than or equal to K, then reverse the last subarray (irrespective of its size). You shouldn't return any array, modify the given array in-place.

Example 1:

Input:
N = 5, K = 3
arr[] = {1,2,3,4,5}
Output: 3 2 1 5 4
Explanation: First group consists of elements
1, 2, 3. Second group consists of 4,5.
 

Example 2:

Input:
N = 4, K = 3
arr[] = {5,6,8,9}
Output: 8 6 5 9
 

Your Task:
You don't need to read input or print anything. The task is to complete the function reverseInGroups() which takes the array, N and K as input parameters and modifies the array in-place. (Please write program in python)
'''


def reverseInGroups(arr, N, K):

    for i in range(0, N, K):

        start = i
        end = min(i + K - 1, N - 1)

        # Reverse the sub-array
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

# Example usage:
arr1 = [1, 2, 3, 4, 5]
N1 = 5
K1 = 3
reverseInGroups(arr1, N1, K1)
print(arr1)  # Output: [3, 2, 1, 5, 4]

arr2 = [5, 6, 8, 9]
N2 = 4
K2 = 3
reverseInGroups(arr2, N2, K2)
print(arr2)  # Output: [8, 6, 5, 9]
