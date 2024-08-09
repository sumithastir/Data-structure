'''
Problem Description
Given an integer A.
Two numbers, X and Y, are defined as follows:

X is the greatest number smaller than A such that the XOR sum of X and A is the same as the sum of X and A.
Y is the smallest number greater than A, such that the XOR sum of Y and A is the same as the sum of Y and A.
Find and return the XOR of X and Y.

NOTE 1: XOR of X and Y is defined as X ^ Y where '^' is the BITWISE XOR operator.
NOTE 2: Your code will be run against a maximum of 100000 Test Cases.

Problem Constraints
1 <= A <= 109

Input Format
First and only argument is an integer A.

Output Format
Return an integer denoting the XOR of X and Y.

Example Input
A = 5

Example Output
10

Example Explanation
The value of X will be 2 and the value of Y will be 8. The XOR of 2 and 8 is 10.
'''


class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        # Optimize Approach

        X = 0
        Y = 0
        i = 0

        while A > 0:
            if (A & 1) == 0:
                X = X | (1 << i)
            A = A >> 1
            i += 1
        Y = 1 << i
        return X ^ Y

        # X = 0
        # i = 0

        # calc X first
        # while((A >> i) != 0):
        #     if((A & (1 << i)) == 0):
        #         X |= (1 << i)
        #     i+=1
        # Y = 2**i
        # return X ^ Y # (int)Math.pow(2,i) is Y, since it is smallest number greater than A

A = 5
obj = Solution()
obj.solve(A)