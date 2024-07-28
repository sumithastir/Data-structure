'''
Problem Description
Imagine a histogram where the bars' heights are given by the array A. Each bar is of uniform width, which is 1 unit. When it rains, water will accumulate in the valleys between the bars.

Your task is to calculate the total amount of water that can be trapped in these valleys.

Example:

The Array A = [5, 4, 1, 4, 3, 2, 7] is visualized as below. The total amount of rain water trapped in A is 11.


Rain Water Trapped




Problem Constraints
1 <= |A| <= 105
0 <= A[i] <= 105



Input Format
First and only argument is the Integer Array, A.



Output Format
Return an Integer, denoting the total amount of water that can be trapped in these valleys



Example Input
Input 1:

 A = [0, 1, 0, 2]
Input 2:

A = [1, 2]


Example Output
Output 1:

1
Output 2:

0


Example Explanation
Explanation 1:

1 unit is trapped on top of the 3rd element.
Rain Water Histogram
Explanation 2:

No water is trapped.
'''


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def trap(self, A):
        N = len(A)
        lmax = [0] * N
        rmax = [0] * N
        lmax[0] = A[0]
        for i in range(1, N):
            lmax[i] = max(lmax[i - 1], A[i])

        rmax[N - 1] = A[N - 1]
        for i in range(N - 2, -1, -1):
            rmax[i] = max(rmax[i + 1], A[i])
        # print(rmax)
        ans = 0
        for i in range(N):
            ans += min(lmax[i], rmax[i]) - A[i]

        return ans


A = [0, 1, 0, 2]
obj = Solution()
obj.trap(A)