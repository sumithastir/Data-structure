'''
Problem Description
Given an array A of N non-negative numbers and a non-negative number B,
you need to find the number of subarrays in A with a sum less than B.
We may assume that there is no overflow.



Problem Constraints
1 <= N <= 5 x 103

1 <= A[i] <= 1000

1 <= B <= 107



Input Format
First argument is an integer array A.

Second argument is an integer B.



Output Format
Return an integer denoting the number of subarrays in A having sum less than B.



Example Input
Input 1:

 A = [2, 5, 6]
 B = 10
Input 2:

 A = [1, 11, 2, 3, 15]
 B = 10


Example Output
Output 1:

 4
Output 2:

 4


Example Explanation
Explanation 1:

 The subarrays with sum less than B are {2}, {5}, {6} and {2, 5},
Explanation 2:

 The subarrays with sum less than B are {1}, {2}, {3} and {2, 3}
'''


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        N = len(A)
        cnt = 0
        psum = [A[0]]

        for i in range(1, N):
            psum.append(psum[i - 1] + A[i])
        # print(psum)

        for si in range(0, N):
            for ei in range(si, N):
                tsum = 0
                if si == 0:
                    tsum = psum[ei]
                else:
                    tsum = psum[ei] - psum[si - 1]

                # tsum = 0
                # for k in range(si,ei+1):
                #     tsum = tsum + A[k]
                #     if tsum > B:
                #         break
                # print(tsum)
                if tsum < B:
                    cnt += 1

        return cnt

# Function Call
A = [2, 5, 6]
B = 10

obj = Solution()
res = obj.solve(A, B)
print(res)