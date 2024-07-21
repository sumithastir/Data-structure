'''
Problem Description
You will be given an integer n. You need to return the count of prime numbers less than or equal to n.


Problem Constraints
0 <= n <= 10^3


Input Format
Single input parameter n in function.


Output Format
Return the count of prime numbers less than or equal to n.


Example Input
Input 1:
19
Input 2:
1


Example Output
Output 1:
8
Output 2:
0


Example Explanation
Explanation 1:
Primes <= 19 are 2, 3, 5, 7, 11, 13, 17, 19
Explanation 2:
There are no primes <= 1
'''


class Solution:
    def factorCount(self, N):
        count = 0
        i = 1
        while i * i <= N:
            if i == N / i:
                count += 1
            elif N % i == 0:
                count += 2
            i += 1
        return count

    # @param A : integer
    # @return an integer
    def solve(self, A):
        count_of_prime_number = 0

        if A == 1: return count_of_prime_number

        for N in range(2, A + 1):
            if self.factorCount(N) == 2:
                count_of_prime_number += 1
        return count_of_prime_number


# Function Call
A = 19
obj = Solution()
res = obj.solve(A)
print(res)