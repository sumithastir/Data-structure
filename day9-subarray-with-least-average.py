'''
Problem Description
Given an array A of size N, find the subarray of size B with the least average.



Problem Constraints
1 <= B <= N <= 105
-105 <= A[i] <= 105


Input Format
First argument contains an array A of integers of size N.
Second argument contains integer B.


Output Format
Return the index of the first element of the subarray of size B that has least average.
Array indexing starts from 0.


Example Input
Input 1:
A = [3, 7, 90, 20, 10, 50, 40]
B = 3
Input 2:

A = [3, 7, 5, 20, -10, 0, 12]
B = 2


Example Output
Output 1:
3
Output 2:

4


Example Explanation
Explanation 1:
Subarray between indexes 3 and 5
The subarray {20, 10, 50} has the least average
among all subarrays of size 3.
Explanation 2:

 Subarray between [4, 5] has minimum average
'''


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        #         1) Initialize res_index = 0 // Beginning of result index
        # 2) Find sum of first B elements. Let this sum be 'curr_sum'
        # 3) Initialize min_sum = sum
        # 4) Iterate from (B+1)'th to n'th element, do following
        #    for every element arr[i]
        #       a) curr_sum = curr_sum + arr[i] - arr[i-B]
        #       b) If curr_sum < min_sum
        #            res_index = (i-B+1)
        # 5) Return res_index as beginning index of resultant subarray.
        N = len(A)
        l = 0
        r = B
        res_index = 0
        curr_sum = 0
        for i in range(0, B):
            curr_sum += A[i]
        min_sum = curr_sum

        for i in range(B, N):
            curr_sum = curr_sum + A[i] - A[i - B]
            if curr_sum < min_sum:
                min_sum = curr_sum
                res_index = (i - B + 1)
        return res_index

# Function Call
A = [3, 7, 90, 20, 10, 50, 40]
B = 3

obj = Solution()
res = obj.solve(A, B)
print(res)