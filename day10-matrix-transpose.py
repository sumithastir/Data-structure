'''
Problem Description
Given a 2D integer array A, return the transpose of A.

The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.


Problem Constraints
1 <= A.size() <= 1000

1 <= A[i].size() <= 1000

1 <= A[i][j] <= 1000



Input Format
First argument is a 2D matrix of integers.



Output Format
You have to return the Transpose of this 2D matrix.



Example Input
Input 1:

A = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
Input 2:

A = [[1, 2],[1, 2],[1, 2]]


Example Output
Output 1:

[[1, 4, 7], [2, 5, 8], [3, 6, 9]]
Output 2:

[[1, 1, 1], [2, 2, 2]]


Example Explanation
Explanation 1:

Clearly after converting rows to column and columns to rows of [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
 we will get [[1, 4, 7], [2, 5, 8], [3, 6, 9]].
Explanation 2:

After transposing the matrix, A becomes [[1, 1, 1], [2, 2, 2]]
'''


class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):
        N = len(A)
        M = len(A[0])
        if N == M:
            for i in range(0, N - 1):
                for j in range(i + 1, N):
                    temp = A[i][j]
                    A[i][j] = A[j][i]
                    A[j][i] = temp
            return A
        else:
            matrix = [[0 for x in range(N)] for y in range(M)]
            for i in range(0, N):
                for j in range(0, M):
                    matrix[j][i] = A[i][j]

            return matrix

# Function Call

A = [[1, 2, 3],
[4, 5, 6],
[7, 8, 9]]

obj = Solution()
res = obj.solve(A)
print(res)