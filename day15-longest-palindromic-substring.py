'''Problem Description
Given a string A of size N, find and return the longest palindromic substring in A.
Substring of string A is A[i...j] where 0 <= i <= j < len(A)

Palindrome string:
A string which reads the same backwards. More formally, A is palindrome if reverse(A) = A.
Incase of conflict, return the substring which occurs first ( with the least starting index).

Problem Constraints
1 <= N <= 6000

Input Format
First and only argument is a string A.

Output Format
Return a string denoting the longest palindromic substring of string A.

Example Input
Input 1:
A = "aaaabaaa"
Input 2:
A = "abba

Example Output
Output 1:
"aaabaaa"
Output 2:
"abba"

Example Explanation
Explanation 1:
We can see that longest palindromic substring is of length 7 and the string is "aaabaaa".
Explanation 2:
We can see that longest palindromic substring is of length 4 and the string is "abba".'''


class Solution:
    # @param A : string
    # @return a strings

    def expand(self, S, i, j):
        N = len(S)
        while i >= 0 and j < N:
            if S[i] != S[j]:
                break
            i -= 1
            j += 1
        return S[i + 1: j]

    def longestPalindrome(self, A):

        # Optimal Approach
        N = len(A)
        ans = 1
        res = A[0]
        for i in range(0, N):
            l1 = self.expand(A, i, i)
            l2 = self.expand(A, i - 1, i)
            if len(l1) > ans:
                ans = len(l1)
                res = l1
            elif len(l2) > ans:
                res = l2
                ans = len(l2)

        return res

# Function Call
A = "aaaabaaa"
obj = Solution()
res = obj.longestPalindrome(A)
print(res)