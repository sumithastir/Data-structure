'''
Problem Description
Given an array A of size N, write a recursive function that returns the maximum element of the array.

Problem Constraints
1 <= N <= 100
1 <= A[i] <= 1000

Input Format
The first line contains the array A.

Output Format
A single integer is the maximum value of the array.

Example Input
Input 1:
A = [12, 10, 3, 4, 5]
Input 2:
A = [1, 5, 80, 40]

Example Output
Output 1:

12
Output 2:
80

Example Explanation
Explanation 1:
 The Maximum element of the array A, [12, 10, 3, 4, 5] is 12
Explanation 2:
 The Maximum element of the array A, [1, 5, 80, 40] is 80
'''

class Solution:
    def get_innerMax(self, A, idx):
        if idx == len(A) -1:
            return A[idx]
        ans = A[idx]
        return max(self.get_innerMax(A, idx+1), ans)
    # @param A : list of integers
    # @return an integer
    def getMax(self, A):
        return self.get_innerMax(A, 0)

A = [12, 10, 3, 4, 5]
obj = Solution()
obj.getMax(A)

