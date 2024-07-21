'''
Problem Description
Given a number A. Return 1 if A is prime and return 0 if not.

Note :
The value of A can cross the range of Integer.


Problem Constraints
1 <= A <= 109


Input Format
The first argument is a single integer A.


Output Format
Return 1 if A is prime else return 0.


Example Input
Input 1:
A = 5
Input 2:

A = 10


Example Output
Output 1:
1
Output 2:

0


Example Explanation
Explanation 1:
5 is a prime number.
Explanation 2:

10 is not a prime number.
'''

class Solution:
    def factorCount(self, A):
        count = 0
        i = 1
        while i*i <= A:
            if i == A/i:
                count +=1
            elif A%i == 0:
                count +=2
            i+=1
        return count

    # @param A : integer
    # @return an integer
    def solve(self, A):
        if A == 1: return 0
        if self.factorCount(A) == 2:
            return 1
        return 0

# Function Call
A = 5

obj = Solution()
res = obj.solve(A)
print(res)