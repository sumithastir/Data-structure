'''
Problems Statement:
You are working on a project to analyze profit for a given set of days. you have been given an array A with profit for N days.
You also have Q queries represented by a 2D array B of size Q*2. Each query consists of two integers B[i][0] and B[i][1].

For every query, your task is to find the count of non-negative profit in the range from A[B[i][0]] to A[B[i][1]]

Problem Constraints:
|A| = N
|B| = Q
1 <= N,Q <= 10^5
-10^9 <= A[i] <= 10^9
0 <= B[i][0] <= B[i][1] <= N-1

Input Format:
First argument A, is an array
Second argument B, is a matrix

Output Format:
Return an array

Example input:
Input 1:
A = [1, -1, 0]
B = [[0, 2],
     [1, 2]]
Input 1:
A = [-1, -2]
B = [[0,0],
     [1,1]]

Example Output:
Output1: [2, 1]
Output2: [0,0]

'''

class Solution:
    def solve(self, A, B):
        pass

A = [1, -1, 0]
B = [[0, 2],
     [1, 2]]
S = Solution()
S.solve(A, B)

