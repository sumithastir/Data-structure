'''
Problems Statement:
You are given a character string A having length N, consisting of only lowercase and uppercase latin letters
You have to toggle case of each character of string A. For e.g 'A' is changed to 'a','e' is changed to 'E', etc.

Problem Constraints:
1 <= N <= 10^5
A[i] must be only from ['a'-'z', 'A'-'Z']

Input Format:
First and only argument is a character string A

Output Format:
Return a character string

example input:
Input 1:  A = "Hello"
Input 1:  A = "tHiSiSaStRiNg"

Example Output:
Output1: hELLO
Output2: ThIsIsAsTrInG

'''

class Solution:
    def solve(self, s):
        N = len(s)
        arr = list(s)
        for i in range(0, N):
            if ord(arr[i]) >= 65 and ord(arr[i]) <= 90:
                arr[i] = chr(ord(arr[i]) + 32)
            elif ord(arr[i]) >= 97 and ord(arr[i]) <= 122:
                arr[i] = chr(ord(arr[i]) - 32)
        return "".join(arr)
print("Test Example 1")
obj = Solution()
s = "hELLO"
print(obj.solve(s))
print("Test Example 1")
s="ThIsIsAsTrInG"
print(obj.solve(s))


