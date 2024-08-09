'''
Problem Description
Given an array A. For every pair of indices i and j (i != j), find the maximum A[i] & A[j].

Problem Constraints
1 <= len(A) <= 105
1 <= A[i] <= 109

Input Format
The first argument is an integer array A.

Output Format
Return a single integer that is the maximum A[i] & A[j].

Example Input
Input 1:-
A = [53, 39, 88]
Input 2:-
A = [38, 44, 84, 12]

Example Output
Output 1:-
37
Output 2:-
36

Example Explanation
Explanation 1:-
53 & 39 = 37
39 & 88 = 0
53 & 88 = 16
Maximum among all these pairs is 37
Explanation 2:-
Maximum bitwise and among all pairs is (38, 44) = 36
'''


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        N = len(A)
        ans = 0

        for i in range(30, -1, -1):
            count = 0
            for j in range(N):
                if (A[j] & (1 << i)) != 0:
                    count += 1
            if count >= 2:
                ans = (ans | (1 << i))
                for j in range(N):
                    if (A[j] & (1 << i)) == 0:
                        A[j] = 0

        return ans

        # N = len(A)
        # ans = 0

        # for i in range(N):
        #     for j in range(i+1, N):
        #         ans = max(ans, (A[i] & A[j]))
        # return ans

A = [53, 39, 88]
obj = Solution()
obj.solve(A)