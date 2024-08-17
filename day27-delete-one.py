'''
Problem Description
Given an integer array A of size N. You have to delete one element such that the GCD(Greatest common divisor) of the remaining array is maximum.

Find the maximum value of GCD.

Problem Constraints
2 <= N <= 105
1 <= A[i] <= 109

Input Format
First argument is an integer array A.

Output Format
Return an integer denoting the maximum value of GCD.

Example Input
Input 1:

 A = [12, 15, 18]
Input 2:

 A = [5, 15, 30]


Example Output
Output 1:

 6
Output 2:

 15

Example Explanation
Explanation 1:

 If you delete 12, gcd will be 3.
 If you delete 15, gcd will be 6.
 If you delete 18, gcd will 3.
 Maximum value of gcd is 6.
Explanation 2:

 If you delete 5, gcd will be 15.
 If you delete 15, gcd will be 5.
 If you delete 30, gcd will be 5.
 Maximum value of gcd is 15.
'''
# sys


class Solution:
    def gcd(self, A, B):
        if B == 0:
            return A
        return self.gcd(B, A % B)

    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        N = len(A)

        prefix_gcd = [0] * N
        prefix_gcd[0] = A[0]
        for i in range(1, N):
            prefix_gcd[i] = self.gcd(prefix_gcd[i - 1], A[i])

        # print(prefix_gcd)

        suffix_gcd = [0] * N
        suffix_gcd[N - 1] = A[N - 1]
        for i in range(N - 2, -1, -1):
            suffix_gcd[i] = self.gcd(suffix_gcd[i + 1], A[i])
        # print(suffix_gcd)

        ans = 1
        for i in range(N):
            if i == 0:
                ans = max(ans, self.gcd(0, suffix_gcd[i + 1]))
            elif i == N - 1:
                ans = max(ans, self.gcd(prefix_gcd[i - 1], 0))

            else:
                ans = max(ans, self.gcd(prefix_gcd[i - 1], suffix_gcd[i + 1]))
        return ans



# Call
A = [12, 15, 18]
obj = Solution()
obj.solve(A)