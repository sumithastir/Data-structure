'''
Problem Description
Given an array of integers A and an integer B, find and return the number of pairs in A whose sum is divisible by B.
Since the answer may be large, return the answer modulo (109 + 7).
Note: Ensure to handle integer overflow when performing the calculations.

Problem Constraints
1 <= length of the array <= 100000
1 <= A[i] <= 109
1 <= B <= 106

Input Format
The first argument given is the integer array A.
The second argument given is the integer B.

Output Format
Return the total number of pairs for which the sum is divisible by B modulo (109 + 7).

Example Input
Input 1:

 A = [1, 2, 3, 4, 5]
 B = 2
Input 2:

 A = [5, 17, 100, 11]
 B = 28

Example Output
Output 1:

 4
Output 2:

 1

Example Explanation
Explanation 1:
 All pairs which are divisible by 2 are (1,3), (1,5), (2,4), (3,5).
 So total 4 pairs.
Explanation 2:
 There is only one pair which is divisible by 28 is (17, 11)
'''


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        freq = [0] * B
        mod = 10 ** 9 + 7
        N = len(A)
        for i in range(N):
            freq[A[i] % B] += 1

        ans = 0
        ans += (freq[0] * (freq[0] - 1)) // 2  #
        if B % 2 == 0:  # if m is a even number then we know m/2 is going to pair it self
            ans += (freq[B // 2] * (freq[B // 2] - 1)) // 2  #
        l = 1
        r = B - 1
        while l < r:
            ans += (freq[l] * freq[r])
            l += 1
            r -= 1
        return ans % mod

# Call
A = [1, 2, 3, 4, 5]
B = 2
obj = Solution()
obj.solve(A,B)