'''
Problem Description
You are given an array A of integers of size N.

Your task is to find the equilibrium index of the given array

The equilibrium index of an array is an index such that the sum of elements at lower indexes is equal to the sum of elements at higher indexes.

If there are no elements that are at lower indexes or at higher indexes, then the corresponding sum of elements is considered as 0.

Note:

Array indexing starts from 0.
If there is no equilibrium index then return -1.
If there are more than one equilibrium indexes then return the minimum index.


Problem Constraints
1 <= N <= 105
-105 <= A[i] <= 105


Input Format
First arugment is an array A .


Output Format
Return the equilibrium index of the given array. If no such index is found then return -1.


Example Input
Input 1:
A = [-7, 1, 5, 2, -4, 3, 0]
Input 2:

A = [1, 2, 3]


Example Output
Output 1:
3
Output 2:

-1


Example Explanation
Explanation 1:
i   Sum of elements at lower indexes    Sum of elements at higher indexes
0                   0                                   7
1                  -7                                   6
2                  -6                                   1
3                  -1                                  -1
4                   1                                   3
5                  -3                                   0
6                   0                                   0

3 is an equilibrium index, because:
A[0] + A[1] + A[2] = A[4] + A[5] + A[6]
Explanation 1:

i   Sum of elements at lower indexes    Sum of elements at higher indexes
0                   0                                   5
1                   1                                   3
2                   3                                   0
Thus, there is no such index.
'''

class Solution:
    # @param A : list of integers
    # @return an integer

    def solve(self, A):
#         1) Initialize leftsum  as 0
# 2) Get the total sum of the array as sum
# 3) Iterate through the array and for each index i, do following.
#     a)  Update sum to get the right sum.
#            sum = sum - arr[i]
#        // sum is now right sum
#     b) If leftsum is equal to sum, then return current index.
#        // update leftsum for next iteration.
#     c) leftsum = leftsum + arr[i]
# 4) return -1
# // If we come out of loop without returning then
# // there is no equilibrium index
        leftsum = 0
        totalsum = sum(A)
        N = len(A)
        for i in range(0, N):
            totalsum = totalsum - A[i]
            if leftsum == totalsum:
                return i
            leftsum = leftsum + A[i]
        return -1


# Function Call
A = [-7, 1, 5, 2, -4, 3, 0]

obj = Solution()
res = obj.solve(A)
print(res)