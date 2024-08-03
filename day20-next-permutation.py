'''
Problem Description
Implement the next permutation, which rearranges numbers into the numerically next greater permutation of numbers
for a given array A of size N.
If such arrangement is not possible, it must be rearranged as the lowest possible order,
i.e., sorted in ascending order.

NOTE:
The replacement must be in-place, do not allocate extra memory.
DO NOT USE LIBRARY FUNCTION FOR NEXT PERMUTATION.
Use of Library functions will disqualify your submission retroactively and will give you penalty points.

Problem Constraints
1 <= N <= 5 * 105
1 <= A[i] <= 109

Input Format
The first and the only argument of input has an array of integers, A.

Output Format
Return an array of integers, representing the next permutation of the given array.

Example Input
Input 1:
A = [1, 2, 3]

Input 2:
A = [3, 2, 1]


Example Output
Output 1:

 [1, 3, 2]
Output 2:

 [1, 2, 3]


Example Explanation
Explanation 1:

 Next permutaion of [1, 2, 3] will be [1, 3, 2].
Explanation 2:

 No arrangement is possible such that the number are arranged into the numerically next greater permutation of numbers.
 So will rearranges it in the lowest possible order.
'''


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def reverse(self, A, si, ei):
        l = si
        r = ei
        while l < r:
            A[l], A[r] = A[r], A[l]
            l += 1
            r -= 1
        return A

    def nextPermutation(self, A):
        # This is very Tricky Solution . Watch Hint Video can help you to understand this.

        N = len(A)
        r = N - 1
        if N == 1:
            return A
        while r > 0:
            if A[r] > A[r - 1]:
                x = r - 1
                y = r
                while y < N:
                    if A[y] < A[x]:
                        break
                    y += 1
                A[y - 1], A[x] = A[x], A[y - 1]
                si = r
                ei = N - 1
                A = self.reverse(A, si, ei)
                break
            r -= 1
        if r == 0:
            A.sort()
        return A

A = [1, 2, 3]
obj = Solution()
obj.nextPermutation(A)