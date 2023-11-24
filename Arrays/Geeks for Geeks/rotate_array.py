'''
Given an unsorted array arr[] of size N. Rotate the array to the left (counter-clockwise direction) by D steps, where D is a positive integer. 

 

Example 1:

Input:
N = 5, D = 2
arr[] = {1,2,3,4,5}
Output: 3 4 5 1 2
Explanation: 1 2 3 4 5  when rotated
by 2 elements, it becomes 3 4 5 1 2.
Example 2:

Input:
N = 10, D = 3
arr[] = {2,4,6,8,10,12,14,16,18,20}
Output: 8 10 12 14 16 18 20 2 4 6
Explanation: 2 4 6 8 10 12 14 16 18 20 
when rotated by 3 elements, it becomes 
8 10 12 14 16 18 20 2 4 6.
 

Your Task:
You need not print or read anything. You need to complete the function rotateArr() which takes the array, D and N as input parameters and rotates the array by D elements. The array must be modified in-place without using extra space. 

 

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

 

Constraints:
1 <= N <= 106
1 <= D <= 106
0 <= arr[i] <= 105


'''


def rotateArr(arr, D, N):

    D = D % N
    while D % N > N:
        D = D % N

    # Reverse the first D elements
    reverse(arr, 0, D - 1)
    # Reverse the remaining N-D elements
    reverse(arr, D, N - 1)
    # Reverse the entire array
    reverse(arr, 0, N - 1)

def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

# Example usage:
arr1 = [1, 2, 3, 4, 5]
N1 = 5
D1 = 2
rotateArr(arr1, D1, N1)
print(arr1)  # Output: [3, 4, 5, 1, 2]

arr2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
N2 = 10
D2 = 3
rotateArr(arr2, D2, N2)
print(arr2)  # Output: [8, 10, 12, 14, 16, 18, 20, 2, 4, 6]
