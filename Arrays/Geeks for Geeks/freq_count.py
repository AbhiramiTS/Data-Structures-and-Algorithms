'''
Given an array arr[] of N positive integers which can contain integers from 1 to P where elements can be repeated or can be absent from the array. Your task is to count the frequency of all numbers from 1 to N. Make in-place changes in arr[], such that arr[i] = frequency(i). Assume 1-based indexing.
Note: The elements greater than N in the array can be ignored for counting and do modify the array in-place. 

Example 1:

Input:
N = 5
arr[] = {2, 3, 2, 3, 5}
P = 5
Output:
0 2 2 0 1
Explanation: 
Counting frequencies of each array element
We have:
1 occurring 0 times.
2 occurring 2 times.
3 occurring 2 times.
4 occurring 0 times.
5 occurring 1 time.
Example 2:

Input:
N = 4
arr[] = {3,3,3,3}
P = 3
Output:
0 0 4 0
Explanation: 
Counting frequencies of each array element
We have:
1 occurring 0 times.
2 occurring 0 times.
3 occurring 4 times.
4 occurring 0 times.
Example 3:

Input:
N = 2
arr[] = {8,9}
P = 9
Output:
0 0
Explanation: 
Counting frequencies of each array element
We have:
1 occurring 0 times.
2 occurring 0 times.
Since here P=9, but there are no 9th Index present so can't count the value.
Your Task:
You don't need to read input or print anything. Complete the function frequencyCount() that takes the array arr, and integers n, and p as input parameters and modify the array in-place to denote the frequency count of each element from 1 to N.

Expected time complexity: O(N)
Expected auxiliay space: O(1)

Constraints:
1 ≤ N ≤ 105
1 ≤ P ≤ 4*104 
1 <= arr[i] <= P

'''


def frequencyCount(arr, N, P):

    for i in range(N):
        # Decrease the array element by 1 to make it compatible with 0-based indexing
        arr[i] -= 1

    for i in range(N):
        # Increment the frequency of the corresponding element by P
        arr[arr[i] % N] += N

    for i in range(N):
        # Set the array element to its frequency after division by N
        arr[i] //= N

# TODO




# Example usage:
arr1 = [2, 3, 2, 3, 5]
N1 = 5
P1 = 5
frequencyCount(arr1, N1, P1)
print(arr1)  # Output: [0, 2, 2, 0, 1]

arr2 = [3, 3, 3, 3]
N2 = 4
P2 = 3
# frequencyCount(arr2, N2, P2)
print(arr2)  # Output: [0, 0, 4, 0]

arr3 = [8, 9]
N3 = 2
P3 = 9
# frequencyCount(arr3, N3, P3)
print(arr3)  # Output: [0, 0]
