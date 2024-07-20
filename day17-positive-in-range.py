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
        N = len(A)
        psum = [0]* N
        if A[0] >= 0:
            psum[0] = 1
        for i in range(1, N):
            if A[i] >= 0:
                psum[i] = psum[i-1] + 1
            else:
                psum[i] = psum[i - 1]

        res = []
        for i in range(0, len(B)):
            l = B[i][0]
            r = B[i][1]
            if l == 0:
                res.append(psum[r])
            else:
                res.append(psum[r] - psum[l-1])
        return res

print("Test Example 1")
A = [1, -1, 0]
B = [[0, 2],
     [1, 2]]
S = Solution()
print(S.solve(A, B))
print("Test Example 2")
A = [-1, -2]
B = [[0,0],
     [1,1]]
S = Solution()
print(S.solve(A, B))

