'''
Problem Description
You are given an array of integers A of size N.
The value of a subarray is defined as BITWISE OR of all elements in it.
Return the sum of value of all subarrays of A % 109 + 7.

Problem Constraints
1 <= N <= 105
1 <= A[i] <= 108

Input Format
The first argument given is the integer array A.

Output Format
Return the sum of Value of all subarrays of A % 109 + 7.

Example Input
Input 1:
 A = [1, 2, 3, 4, 5]
Input 2:
 A = [7, 8, 9, 10]

Example Output
Output 1:
 71
Output 2:
 110

Example Explanation
Explanation 1:

 Value([1]) = 1
 Value([1, 2]) = 3
 Value([1, 2, 3]) = 3
 Value([1, 2, 3, 4]) = 7
 Value([1, 2, 3, 4, 5]) = 7
 Value([2]) = 2
 Value([2, 3]) = 3
 Value([2, 3, 4]) = 7
 Value([2, 3, 4, 5]) = 7
 Value([3]) = 3
 Value([3, 4]) = 7
 Value([3, 4, 5]) = 7
 Value([4]) = 4
 Value([4, 5]) = 5
 Value([5]) = 5
 Sum of all these values = 71
Explanation 2:

 Sum of value of all subarray is 110.
'''


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        # Explained Optimize Approach
        N = len(A)
        subarr_count = (N * (N + 1)) // 2
        ans = 0
        mod = 10 ** 9 + 7
        for pos in range(32):
            zero_sub = 0
            zero_val = 0

            for i in range(N):
                if (A[i] & (1 << pos)) == 0:

                    zero_val = zero_val + 1
                else:
                    zero_sub += ((zero_val * (zero_val + 1)) // 2)
                    zero_val = 0

            if zero_val > 0:
                zero_sub += ((zero_val * (zero_val + 1)) // 2)

            ans = (ans + ((subarr_count - zero_sub) * (1 << pos))) % mod

        return ans % mod

        # Optimize as copied from dicussion
        # ans = 0
        # mod = 10**9 + 7
        # N = len(A)
        # # We assume integers are 32-bit
        # for num in range(31):
        #     index = -1
        #     for i in range(N):
        #         if (A[i] >> num) & 1:
        #             ans += (2 ** num) * (i - index) * (N - i)
        #             index = i
        #     ans  = ans % mod
        # return ans

        # brute Force Approach
        # val = 0
        # N = len(A)
        # for i in range(N):
        #     for j in range(i, N):
        #         tsum = 0

        #         for k in range(i,j+1):

        #             tsum = tsum | A[k]

        #         val = val + tsum
        # return val


A = [1, 2, 3, 4, 5]
obj = Solution()
obj.solve(A)