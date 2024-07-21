'''
Problem Description
Given a string A, you are asked to reverse the string and return the reversed string.

Problem Constraints
1 <= |A| <= 105
String A consist only of lowercase characters.

Input Format
First and only argument is a string A.

Output Format
Return a string denoting the reversed string.

Example Input
Input 1:
 A = "scaler"
Input 2:
 A = "academy"

Example Output
Output 1:
 "relacs"
Output 2:
 "ymedaca"

Example Explanation
Explanation 1:
 Reverse the given string.

'''
class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        arr = list(A)
        N = len(A)
        l = 0
        r = N-1

        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l+=1
            r-=1
        return "".join(arr)

# Function Call
A = "scaler"
obj = Solution()
res = obj.solve(A)
print(res)
