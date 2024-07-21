'''Problem Description
You are given a string A of size N.
Return the string A after reversing the string word by word.

NOTE:
A sequence of non-space characters constitutes a word.
Your reversed string should not contain leading or trailing spaces, even if it is present in the input string.
If there are multiple spaces between words, reduce them to a single space in the reversed string.

Problem Constraints
1 <= N <= 3 * 105

Input Format
The only argument given is string A.

Output Format
Return the string A after reversing the string word by word.

Example Input
Input 1:
A = "the sky is blue"
Input 2:
A = "this is ib"

Example Output
Output 1:
"blue is sky the"
Output 2:
"ib is this"

Example Explanation
Explanation 1:
We reverse the string word by word so the string becomes "blue is sky the".
Explanation 2:
We reverse the string word by word so the string becomes "ib is this".'''

class Solution:
    # @param A : string
    # @return a strings
    def reverse(self, A):
        N = len(A)
        l = 0
        r = N-1

        while l < r:

            A[l], A[r] = A[r], A[l]
            l+=1
            r-=1
        return " ".join(A)

    def solve(self, A):
        arr = A.split(" ")
        N = len(arr)
        for i in range(0, N):
            arr[i] = arr[i].strip()
        # print(arr)
        return self.reverse(arr).strip()

# Function Call
A = "the sky is blue"
obj = Solution()
res = obj.solve(A)
print(res)