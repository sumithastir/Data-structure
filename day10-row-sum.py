'''
Problem Constraints
1 <= A.size() <= 103

1 <= A[i].size() <= 103

1 <= A[i][j] <= 103



Input Format
First argument A is a 2D array of integers.(2D matrix).



Output Format
Return an array containing row-wise sums of original matrix.



Example Input
Input 1:

[1,2,3,4]
[5,6,7,8]
[9,2,3,4]


Example Output
Output 1:

[10,26,18]


Example Explanation
Explanation 1

Row 1 = 1+2+3+4 = 10
Row 2 = 5+6+7+8 = 26
Row 3 = 9+2+3+4 = 18
'''

class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        N = len(A)
        M = len(A[0])
        res = []
        for i in range(0, N):
            tsum = 0
            for j in range(0, M):
                tsum+=A[i][j]
            res.append(tsum)
        return res

A = [[1,2,3,4],
[5,6,7,8],
[9,2,3,4]]
obj = Solution()
res = obj.solve(A)
print(res)