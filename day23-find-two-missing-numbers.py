'''
Problem Description
Given an array A of length N where all the elements are distinct and are in the range [1, N+2].
Two numbers from the range [1, N+2] are missing from the array A. Find the two missing numbers.

Problem Constraints
1 <= N <= 105
1 <= A[i] <= N+2

The elements of array A are distinct

Input Format
Only argument A is an array of integers

Output Format
Return a sorted array of size 2 denoting the missing elements.

Example Input
Input 1:
A = [3, 2, 4]
Input 2:
A = [5, 1, 3, 6]

Example Output
Output 1:
[1, 5]
Output 2:
[2, 4]

Example Explanation
For Input 1:
The missing numbers are 1 and 5.
For Input 2:
The missing numbers are 2 and 4.
'''


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        arr = []
        N = len(A)

        for i in range(1, N + 3):
            arr.append(i)
        arr.extend(A)

        val = 0
        arr_len = len(arr)
        for i in range(arr_len):
            val = val ^ arr[i]

        pos = 0
        for i in range(32):
            if (val & (1 << i)) != 0:
                pos = i
                break
        s1 = 0
        s2 = 0
        for i in range(arr_len):
            if (arr[i] & (1 << pos)) == 0:
                s1 = s1 ^ arr[i]
            else:
                s2 = s2 ^ arr[i]

        if s2 > s1:
            return [s1, s2]
        return [s2, s1]



A = [3, 2, 4]
obj = Solution()
obj.solve(A)