'''
Given an array A of positive integers. Your task is to find the leaders in the array. An element of array is leader if it is greater than or equal to all the elements to its right side. The rightmost element is always a leader. 

Example 1:

Input:
n = 6
A[] = {16,17,4,3,5,2}
Output: 17 5 2
Explanation: The first leader is 17 
as it is greater than all the elements
to its right.  Similarly, the next 
leader is 5. The right most element 
is always a leader so it is also 
included.
Example 2:

Input:
n = 5
A[] = {1,2,3,4,0}
Output: 4 0
Explanation: 0 is the rightmost element
and 4 is the only element which is greater
than all the elements to its right.
Your Task:
You don't need to read input or print anything. The task is to complete the function leader() which takes array A and n as input parameters and returns an array of leaders in order of their appearance.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)

Constraints:
1 <= n <= 107
0 <= Ai <= 107


'''


def leaders(A, N):
    #Code here
    leader = A[-1]
    leaders_list = []
    leaders_list.append(leader)
    for i in range(len(A)-2, -1, -1):
        if A[i] >= leader:
            leader = A[i]
            leaders_list.append(A[i])
            
            
    return leaders_list[::-1]




arr1 = [16, 17, 4, 3, 5, 2]
n1 = 6
print(leaders(arr1, n1))  # Output: [17, 5, 2]

arr2 = [1, 2, 3, 4, 0]
n2 = 5
print(leaders(arr2, n2))  # Output: [4, 0]