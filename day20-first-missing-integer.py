'''
Problem Description
Given an unsorted integer array, A of size N. Find the first missing positive integer.
Note: Your algorithm should run in O(n) time and use constant space.

Problem Constraints
1 <= N <= 1000000
-10^9 <= A[i] <= 10^9

Input Format
First argument is an integer array A.

Output Format
Return an integer denoting the first missing positive integer.

Example Input

Input 1:
[1, 2, 0]

Input 2:
[3, 4, -1, 1]

Input 3:
[-8, -7, -6]


Example Output
Output 1:

3
Output 2:

2
Output 3:

1

Example Explanation
Explanation 1:

A = [1, 2, 0]
First positive integer missing from the array is 3.
Explanation 2:

A = [3, 4, -1, 1]
First positive integer missing from the array is 2.
Explanation 3:

A = [-8, -7, -6]
First positive integer missing from the array is 1.
'''


class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        N = len(A)

        for i in range(N):
            if A[i] <= 0:
                A[i] = N + 2
        # print(A)
        for i in range(N):
            B = abs(A[i]) - 1
            if B < N:
                # print(B)
                A[B] = - abs(A[B])

        # print(A)
        for i in range(N):
            if A[i] >= 0:
                return i + 1
        # print("Yes")
        return N + 1

A = [1, 2, 0]
obj = Solution()
obj.firstMissingPositive(A)