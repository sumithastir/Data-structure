'''
Problem Description
Given a non-negative number represented as an array of digits, add 1 to the number ( increment the number represented by the digits ).

The digits are stored such that the most significant digit is at the head of the list.

NOTE: Certain things are intentionally left unclear in this question which you should practice asking the interviewer. For example: for this problem, the following are some good questions to ask :

Q: Can the input have 0's before the most significant digit. Or, in other words, is 0 1 2 3 a valid input?
A: For the purpose of this question, YES
Q: Can the output have 0's before the most significant digit? Or, in other words, is 0 1 2 4 a valid output?
A: For the purpose of this question, NO. Even if the input has zeroes before the most significant digit.


Problem Constraints
1 <= size of the array <= 1000000



Input Format
First argument is an array of digits.



Output Format
Return the array of digits after adding one.



Example Input
Input 1:

[1, 2, 3]


Example Output
Output 1:

[1, 2, 4]


Example Explanation
Explanation 1:

Given vector is [1, 2, 3].
The returned vector should be [1, 2, 4] as 123 + 1 = 124.
'''


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):

        N = len(A)
        # count the zeros if Array length is greater than 1
        if N > 1:
            zeros = 0
            i = 0
            while A[i] == 0:
                zeros += 1
                i += 1
            N = N - zeros
        # Reverse the Array
        A.reverse()
        num = 0
        arr = []
        for i in range(N):
            if i == 0:
                num = (A[i] + 1)
            else:
                num = (carry + A[i])

            carry = num // 10
            r = num % 10
            arr.append(r)

        if carry > 0:
            arr.append(carry)

        arr.reverse()

        return arr


A = [0, 1, 0, 2]
obj = Solution()
obj.plusOne(A)