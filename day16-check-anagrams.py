'''
Problems Statement:
You are given two lowercase strings A and B each of length N. Return 1 if they are anagrams to each other and 0 if not.

Note : Two strings A and B are called anagrams to each other if A can be formed after rearranging the letters of B.



Problem Constraints:
1 <= N <= 105
A and B are lowercase strings

Input Format:
Both arguments A and B are a string.

Output Format:
Return 1 if they are anagrams and 0 if not

Example input:
Input 1:
A = "cat"
B = "bat"
Input 2:
A = "secure"
B = "rescue"


Example Output
Output 1:
0
Output 2:
1

Example Explanation
For Input 1:
The words cannot be rearranged to form the same word. So, they are not anagrams.
For Input 2:
They are an anagram.

'''


class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        arr = [0] * 26
        arr1 = [0] * 26
        N = len(A)

        for i in range(N):
            arr[ord(A[i]) - ord('a')] += 1
            arr1[ord(B[i]) - ord('a')] += 1

        for i in range(0, 26):
            if arr[i] != arr1[i]:
                return 0
        return 1

A = "cat"
B = "bat"
obj = Solution()
res = obj.solve(A, B)
print(res)

