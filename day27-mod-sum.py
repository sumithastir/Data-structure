'''
Problem Description
Given an array of integers A, calculate the sum of A [ i ] % A [ j ] for all possible i, j pairs. Return sum % (109 + 7) as an output.

Problem Constraints
1 <= length of the array A <= 105

1 <= A[i] <= 103

Input Format
The only argument given is the integer array A.

Output Format
Return a single integer denoting sum % (109 + 7).

Example Input
Input 1:

 A = [1, 2, 3]
Input 2:

 A = [17, 100, 11]

Example Output
Output 1:

 5
Output 2:

 61

Example Explanation
Explanation 1:

 (1 % 1) + (1 % 2) + (1 % 3) + (2 % 1) + (2 % 2) + (2 % 3) + (3 % 1) + (3 % 2) + (3 % 3) = 5
'''


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        '''
        Calculate the frequency of all the elements from 1 to 1000.
For all values i from 1 to 1000 calculate sumi as sum of i % A[j] , where 1 <= j <= n
Sum of all such ((sumi) * (frequency of i)) would be the final answer.'''

        freq = [0] * 1001
        mod = 10 ** 9 + 7
        # N = len(A)
        for i in A:
            freq[i] += 1

        ans = 0
        for i in range(1, 1001):
            for j in range(1, 1001):
                val = i % j
                temp = freq[i] * freq[j] * val
                ans = ((ans % mod) + (temp % mod)) % mod

        return ans

# Call
A = [1, 2, 3]
obj = Solution()
obj.solve(A)
