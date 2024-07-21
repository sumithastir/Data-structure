'''
Problem Description
Find the number of occurrences of bob in string A consisting of lowercase English alphabets.



Problem Constraints
1 <= |A| <= 1000


Input Format
The first and only argument contains the string A, consisting of lowercase English alphabets.


Output Format
Return an integer containing the answer.


Example Input
Input 1:

  "abobc"
Input 2:

  "bobob"


Example Output
Output 1:

  1
Output 2:

  2


Example Explanation
Explanation 1:

  The only occurrence is at second position.
Explanation 2:

  Bob occures at first and third position.
'''


class Solution:
    # @param A : string
    # @return an integer
    def ismatch(self, S1, S2):
        N = len(S1)
        i = 0
        while i < N:
            if S1[i] != S2[i]:
                return False
            i += 1
        return True

    def solve(self, A):
        count = 0
        N = len(A)
        for i in range(0, N - 2):

            if self.ismatch(A[i:i + 3], "bob"):
                count += 1
        return count


# Function Call
A = "abobc"
obj = Solution()
res = obj.solve(A)
print(res)