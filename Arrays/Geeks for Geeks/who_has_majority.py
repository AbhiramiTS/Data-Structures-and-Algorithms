'''
Given an array arr[] of size N and two elements x and y, use counter variables to find which element appears most in the array. If both elements have the same frequency, then return the smaller element.
Note:  We need to return the element, not its count.

 

Example 1:

Input:
N = 11
arr[] = {1,1,2,2,3,3,4,4,4,4,5}
x = 4, y = 5
Output: 4
Explanation: 
frequency of 4 is 4.
frequency of 5 is 1.
 

Example 2:

Input:
N = 8
arr[] = {1,2,3,4,5,6,7,8}
x = 1, y = 7
Output: 1
Explanation: 
frequency of 1 is 1.
frequency of 7 is 1.
Since 1 < 7, return 1.
 

Your Task:
You don't need to read input or print anything. Complete the function majorityWins() that takes array, n, x, y as input parameters and return the element with higher frequency.

 

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

 

Constraints:
1 <= n <= 103
0 <= arri , x , y <= 108

'''


def majorityWins(arr, n, x, y):

    count_x = 0  # Counter for element x
    count_y = 0  # Counter for element y

    for element in arr:
        if element == x:
            count_x += 1
        elif element == y:
            count_y += 1

    if count_x > count_y:
        return x
    elif count_y > count_x:
        return y
    else:
        return min(x, y)



# Example usage:
arr1 = [1, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5]
n1 = 11
x1 = 4
y1 = 5
print(majorityWins(arr1, n1, x1, y1))  # Output: 4

arr2 = [1, 2, 3, 4, 5, 6, 7, 8]
n2 = 8
x2 = 1
y2 = 7
print(majorityWins(arr2, n2, x2, y2))  # Output: 1
