'''Problem Description
Given an integer A, generate a square matrix filled with elements from 1 to A2 in spiral order and return the generated square matrix.



Problem Constraints
1 <= A <= 1000



Input Format
First and only argument is integer A


Output Format
Return a 2-D matrix which consists of the elements added in spiral order.



Example Input
Input 1:

1
Input 2:

2
Input 3:

5


Example Output
Output 1:

[ [1] ]
Output 2:

[ [1, 2],
  [4, 3] ]
Output 3:

[ [1,   2,  3,  4, 5],
  [16, 17, 18, 19, 6],
  [15, 24, 25, 20, 7],
  [14, 23, 22, 21, 8],
  [13, 12, 11, 10, 9] ]


Example Explanation
Explanation 1:

Only 1 is to be arranged.
Explanation 2:

1 --> 2
      |
      |
4<--- 3
Explanation 3:

'''

class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):
        N = A^2

        i = 0
        j = 0
        N = A
        cnt = 1
        metrics = [[0 for i in range(A)] for j in range(A)]

        if A == 1:
            metrics[0][0] = A
            return metrics

        while N > 1:

            for k in range(1, N):
                # print(k)
                metrics[i][j] = cnt
                cnt +=1
                j+=1
            # print(metrics)
            for _ in range(1, N):
                metrics[i][j] = cnt
                cnt +=1
                i+=1

            for _ in range(1, N):
                metrics[i][j] = cnt
                cnt +=1
                j-=1

            for _ in range(1, N):
                metrics[i][j] = cnt
                cnt +=1
                i-=1
            i+=1
            j+=1
            N = N-2
        if N == 1:
            metrics[i][j] = cnt
        return metrics



A = 5

obj = Solution()
obj.generateMatrix(A)