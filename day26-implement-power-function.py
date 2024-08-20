'''
Problem Description
Implement pow(A, B) % C.
In other words, given A, B and C, Find (AB % C).
Note: The remainders on division cannot be negative. In other words, make sure the answer you return is non-negative.

Problem Constraints
-109 <= A <= 109
0 <= B <= 109
1 <= C <= 109

Input Format
Given three integers A, B, C.

Output Format
Return an integer.

Example Input
Input 1:
A = 2
B = 3
C = 3
Input 2:
A = 3
B = 3
C = 1

Example Output
Output 1:
2
Output 2:
0

Example Explanation
Explanation 1:
23 % 3 = 8 % 3 = 2
Explanation 2:
33 % 1 = 27 % 1 = 0
'''


# Do not write code to include libraries, main() function or accept any input from the console.
# Initialization code is already written and hidden from you. Do not write code for it again.
class Solution:
    def find_pow_val(self, A, N, C):

        if N == 0:
            return 1

        power = self.find_pow_val(A, N // 2, C) % C
        power = (power * power) % C

        if N % 2 == 1:
            power = (power * A) % C

        power = (power + C) % C
        return power

    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def pow(self, A, B, C):
        # Just write your code below to complete the function. Required input is available to you as the function arguments.
        # Do not print the result or any output. Just return the result via this function.
        return self.find_pow_val(A, B, C) % C

A = 2
B = 3
C = 3
obj = Solution()
obj.pow(A, B, C)