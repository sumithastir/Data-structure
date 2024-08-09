'''
Problem Description
Given an array of integers A, every element appears twice except for one. Find that integer that occurs once.
NOTE: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Problem Constraints

1 <= |A| <= 2000000
0 <= A[i] <= INTMAX

Input Format
The first and only argument of input contains an integer array A.

Output Format
Return a single integer denoting the single element.

Example Input
Input 1:
 A = [1, 2, 2, 3, 1]
Input 2:
 A = [1, 2, 2]

Example Output
Output 1:
 3

Output 2:
 1

Example Explanation
Explanation 1:

3 occurs once.
Explanation 2:

1 occurs once.
'''
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        # using  bit count method
        # ans = 0
        # N = len(A)
        # for i in range(32):
        #     count = 0
        #     for j in range(N):
        #         if (A[j] & (1<<i)) != 0:
        #             count +=1
        #     if count %2 !=0:
        #          ans = (ans| (1<<i))
        # return ans

        # O(N) Complexity using XOR Keyword
        N = len(A)
        ans = 0
        for i in range(N):
            ans = ans ^ A[i]

        return ans

# Function Call

A = [1, 2, 2, 3, 1]

obj = Solution()
obj.singleNumber(A)
