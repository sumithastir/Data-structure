'''
Problem Description
You have given a string A having Uppercase English letters.

You have to find how many times subsequence "AG" is there in the given string.

NOTE: Return the answer modulo 109 + 7 as the answer can be very large.



Problem Constraints
1 <= length(A) <= 105



Input Format
First and only argument is a string A.



Output Format
Return an integer denoting the answer.



Example Input
Input 1:

 A = "ABCGAG"
Input 2:

 A = "GAB"


Example Output
Output 1:

 3
Output 2:

 0


Example Explanation
Explanation 1:

 Subsequence "AG" is 3 times in given string
Explanation 2:

 There is no subsequence "AG" in the given string.
'''


class Solution:
    # @param A : string
    # @return an integer

    def solve(self, A):
        m = 1000000007
        count = 0
        ans = 0
        N = len(A)
        for i in range(0, N):
            if A[i] == 'A':
                count += 1
            elif A[i] == 'G':
                ans = ans + count
        return ans % m

        # Brute Force Approach
        # count = 0
        # N = len(A)
        # for i in range(0,N):
        #     if A[i] == "A":
        #         for j in range(i, N):
        #             if A[j] == "G":
        #                 count +=1
        # return count


# Function Call
A = "ABCGAG"

obj = Solution()
res = obj.solve(A)
print(res)
