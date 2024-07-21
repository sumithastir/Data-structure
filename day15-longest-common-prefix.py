'''
Problem Description
Given the array of strings A, you need to find the longest string S, which is the prefix of ALL the strings in the array.

The longest common prefix for a pair of strings S1 and S2 is the longest string S which is the prefix of both S1 and S2.

Example: the longest common prefix of "abcdefgh" and "abcefgh" is "abc".

Problem Constraints
0 <= sum of length of all strings <= 1000000

Input Format
The only argument given is an array of strings A.

Output Format
Return the longest common prefix of all strings in A.

Example Input
Input 1:

A = ["abcdefgh", "aefghijk", "abcefgh"]
Input 2:

A = ["abab", "ab", "abcd"];


Example Output
Output 1: "a"
Output 2: "ab"


Example Explanation
Explanation 1:

Longest common prefix of all the strings is "a".
Explanation 2:

Longest common prefix of all the strings is "ab".
'''


class Solution:
    # @param A : list of strings
    # @return a strings
    def commonPre(self, S1, S2):
        ans = ""
        min_len = min(len(S1), len(S2))
        for i in range(0, min_len):

            if S1[i] == S2[i]:
                ans += S1[i]
            else:
                break

        return ans

    def longestCommonPrefix(self, A):
        N = len(A)

        pre = [0] * N
        pre[0] = A[0]

        for i in range(1, N):
            pre[i] = self.commonPre(pre[i - 1], A[i])
        return pre[N - 1]


# Function Call
A = ["abcdefgh", "aefghijk", "abcefgh"]
obj = Solution()
res = obj.longestCommonPrefix(A)
print(res)