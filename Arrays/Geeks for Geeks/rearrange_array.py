"""

Given a sorted array of positive integers. Your task is to rearrange the array elements alternatively i.e first element should be max value, second should be min value, third should be second max, fourth should be second min and so on.
Note: Modify the original array itself. Do it without using any extra space. You do not have to return anything.

Example 1:

Input:
n = 6
arr[] = {1,2,3,4,5,6}
Output: 6 1 5 2 4 3
Explanation: Max element = 6, min = 1, 
second max = 5, second min = 2, and 
so on... Modified array is : 6 1 5 2 4 3.
Example 2:

Input:
n = 11
arr[]={10,20,30,40,50,60,70,80,90,100,110}
Output:110 10 100 20 90 30 80 40 70 50 60
Explanation: Max element = 110, min = 10, 
second max = 100, second min = 20, and 
so on... Modified array is : 
110 10 100 20 90 30 80 40 70 50 60.
Your Task:
The task is to complete the function rearrange() which rearranges elements as explained above. Printing of the modified array will be handled by driver code.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Constraints:
1 <= n <= 10^6
1 <= arr[i] <= 10^7


"""



class Solution:
    def rearrange(self, arr, n):
        # Initialize pointers for the maximum and minimum elements
        max_index = n - 1
        min_index = 0

        # Find a number greater than the maximum element in the array
        max_ele = arr[max_index] + 1

        # Rearrange the array using the given logic
        for i in range(n):
            if i % 2 == 0:
                # For even indices, store the modified element with the maximum element
                arr[i] += (arr[max_index] % max_ele) * max_ele
                max_index -= 1
            else:
                # For odd indices, store the modified element with the minimum element
                arr[i] += (arr[min_index] % max_ele) * max_ele
                min_index += 1

        # Retrieve the original array elements after rearrangement
        for i in range(n):
            arr[i] //= max_ele

# Test cases
if __name__ == "__main__":
    # Example 1
    sol = Solution()
    arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    n1 = len(arr1)
    sol.rearrange(arr1, n1)
    print("Test Case 1:", arr1)  # Output should be [9, 1, 8, 2, 7, 3, 6, 4, 5]

    # Example 2
    arr2 = [10,20,30,40,50,60,70,80,90,100,110]
    n2 = len(arr2)
    sol.rearrange(arr2, n2)
    print("Test Case 2:", arr2)  # Output should be [4, 1, 3, 2]
