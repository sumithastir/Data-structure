'''
Problem Description
You are given an integer A. You have to tell whether it is a perfect number or not.

Perfect number is a positive integer which is equal to the sum of its proper positive divisors.

A proper divisor of a natural number is the divisor that is strictly less than the number.



Problem Constraints
1 <= A <= 106



Input Format
First and only argument contains a single positive integer A.



Output Format
Return 1 if A is a perfect number and 0 otherwise.



Example Input
Input 1:

A = 4
Input 2:

A = 6


Example Output
Output 1:

0
Output 2:

1


Example Explanation
Explanation 1:

For A = 4, the sum of its proper divisors = 1 + 2 = 3, is not equal to 4.
Explanation 2:

For A = 6, the sum of its proper divisors = 1 + 2 + 3 = 6, is equal to 6.
'''

class Solution:

    def sum_of_proper_divisors(self, N):
        count = 0
        i = 1
        while i*i <= N:
            if i == 1:
                count +=1
            elif i == N/i:
                count += i
            elif N % i == 0:
                count += i
                count += N/i
            i+=1
        return count

    # @param A : integer
    # @return an integer
    def solve(self, A):
        if A == 1: return 0
        if self.sum_of_proper_divisors(A) == A:
            return 1
        else:
            return 0


# Function Call
A = 4
obj = Solution()
res = obj.solve(A)
print(res)