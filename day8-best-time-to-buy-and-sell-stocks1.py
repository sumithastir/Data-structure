'''
Problem Description
Say you have an array, A, for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Return the maximum possible profit.



Problem Constraints
0 <= A.size() <= 700000
1 <= A[i] <= 107



Input Format
The first and the only argument is an array of integers, A.


Output Format
Return an integer, representing the maximum possible profit.


Example Input
Input 1:
A = [1, 2]
Input 2:

A = [1, 4, 5, 2, 4]


Example Output
Output 1:
1
Output 2:

4


Example Explanation
Explanation 1:
Buy the stock on day 0, and sell it on day 1.
Explanation 2:

Buy the stock on day 0, and sell it on day 2.
'''


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        max_profit = 0

        N = len(A)
        if N == 0:
            return 0
        maxNumber = A[N - 1]
        i = N - 2
        while i >= 0:
            if A[i] > maxNumber:
                maxNumber = A[i]
            profit = maxNumber - A[i]
            if profit > max_profit:
                max_profit = profit
            i -= 1
        return max_profit
# Brute Force with N^2
# def maxProfit(self, A):
#     max_profit = 0
#     N = len(A)
#     for i in range(0,N):

#         for j in range(i+1, N):
#             max_profit = max(max_profit , A[j]-A[i])


#     return max_profit

# Function Call
A = [1, 2]

obj = Solution()
res = obj.maxProfit(A)
print(res)