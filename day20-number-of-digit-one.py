'''
Problem Description
Given an integer A, find and return the total number of digit 1 appearing in all non-negative integers
less than or equal to A.

Problem Constraints
0 <= A <= 109

Input Format
The only argument given is the integer A.

Output Format
Return the total number of digit 1 appearing in all non-negative integers less than or equal to A.

Example Input
Input 1:
A = 10

Input 2:
 A = 11

Example Output
Output 1:
2

Output 2:
4

Example Explanation
Explanation 1:
Digit 1 appears in 1 and 10 only and appears one time in each. So the answer is 2.

Explanation 2:
Digit 1 appears in 1(1 time) , 10(1 time) and 11(2 times) only. So the answer is 4.
'''

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        ans = 0
        i = 1
        while i <= A:
            ans += ((A //(i*10))* i) + min(max( (A % (i*10)) - (i-1), 0), i)
            i = i* 10
        return ans

A = 10
obj = Solution()
obj.solve(A)