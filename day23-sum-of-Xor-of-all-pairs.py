'''
Problem Description
Given an array A of N integers. Find the sum of bitwise XOR all pairs of numbers in the array.
Since the answer can be large, return the remainder after the dividing the answer by 109+7.

Problem Constraints
1 <= N <= 105
1 <= A[i] < 109

Input Format
Only argument A is an array of integers

Output Format
Return an integer denoting the sum of xor of all pairs of number in the array.

Example Input
Input 1:
A = [1, 2, 3]
Input 2:
A = [3, 4, 2]

Example Output
Output 1:
6
Output 2:
14

Example Explanation
For Input 1:
Pair    Xor
{1, 2}  3
{1, 3}  2
{2, 3}  1
Sum of xor of all pairs = 3 + 2 + 1 = 6.
For Input 2:
Pair    Xor
{3, 4}  7
{3, 2}  1
{4, 2}  6
Sum of xor of all pairs = 7 + 1 + 6 = 14.
'''


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        # optimize Approach
        N = len(A)
        ans = 0
        mod = 10 ** 9 + 7
        for pos in range(32):
            cnt = 0
            for i in range(N):
                if (A[i] & (1 << pos)) != 0:
                    cnt += 1

            if cnt != 0:
                xor = (N - cnt) * cnt
                ans += (2 ** pos) * xor

        return ans % mod

        # Brute for approach But Failed due to Time complexity = N^2
        # ans = 0
        # N = len(A)
        # mod = 10**9 + 7
        # for i in range(N):

        #     tsum = 0
        #     for j in range(i+1, N):
        #         tsum = A[i] ^ A[j]
        #         ans += tsum
        # return ans% mod

A = [1, 2, 3]
obj = Solution()
obj.solve(A)