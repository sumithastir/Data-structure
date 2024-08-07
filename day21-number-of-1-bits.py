'''
Problem Description
Write a function that takes an integer and returns the number of 1 bits present in its binary representation.

Problem Constraints
1 <= A <= 109

Input Format
First and only argument contains integer A

Output Format
Return an integer

Example Input
Input 1:
11
Input 2:
6


Example Output
Output 1:
3
Output 2:
2


Example Explanation
Explaination 1:
11 is represented as 1011 in binary.
Explaination 2:
6 is represented as 110 in binary.
'''

class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        cnt = 0

        for i in range(31):
            if (A & (1<<i)) != 0:
                cnt +=1
        return cnt

A = 11
obj = Solution()
obj.solve(A)