'''
Problem Description
Given an array A, find the size of the smallest subarray such that it contains at least one occurrence of the maximum value of the array

and at least one occurrence of the minimum value of the array.



Problem Constraints
1 <= |A| <= 2000



Input Format
First and only argument is vector A



Output Format
Return the length of the smallest subarray which has at least one occurrence of minimum and maximum element of the array



Example Input
Input 1:

A = [1, 3, 2]
Input 2:

A = [2, 6, 1, 6, 9]


Example Output
Output 1:

 2
Output 2:

 3


Example Explanation
Explanation 1:

 Take the 1st and 2nd elements as they are the minimum and maximum elements respectievly.
Explanation 2:

 Take the last 3 elements of the array.
'''


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        min_val = A[0]
        max_val = A[0]

        for a in A:
            min_val = min(min_val, a)
            max_val = max(max_val, a)

        N = len(A)
        min_inx = max_inx = -1
        ans = N

        for i in range(0, N):
            if min_val == A[i]:
                min_inx = i

                if max_inx != -1:
                    ans = min(ans, min_inx - max_inx + 1)

            if max_val == A[i]:
                max_inx = i
                if min_inx != -1:
                    ans = min(ans, max_inx - min_inx + 1)
        return ans


# Function Call
A = [1, 3, 2]

obj = Solution()
res = obj.solve(A)
print(res)