'''
Problem Description
Given an array of integers A with N elements and a target integer B, the task is to find all the indices
at which B occurs in the array.
Note: The problem encourages recursive logic for learning purposes.
Although the online judge doesn't enforce recursion, it's recommended to use recursive
solutions to align with the question's spirit.

Problem Constraints
1 <= N <= 103
1 <= A[i] <= 103
1 <= B <= 103
It is guaranteed that the target B, exist atleast once in the Array A.

Input Format
First Argument in an Array of Integers, A.
Second Argument is the Target, B.

Output Format
Return the sorted array of indices.

Example Input
Input 1:
A = [1, 2, 3, 4, 5]
B = 1
Input 2:
A = [8, 9, 5, 6, 5, 5]
B = 5

Example Output
Output 1:
[0]
Output 2:
[2, 4, 5]

Example Explanation
Explanation 1:
The Target, 1 occurs on Index = 0.  So returning [0]
Explanation 2:
Here, the target 5 occurs at indexes [2, 4, 5].
'''


class Solution:
    def find_indices(self, A, B, idx, count):
        if idx == len(A):
            arr = [0] * count
            return arr
        if A[idx] == B:
            count += 1

        rr = self.find_indices(A, B, idx + 1, count)
        if A[idx] == B:
            rr[count - 1] = idx
        return rr

    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def allIndices(self, A, B):
        count = 0
        return self.find_indices(A, B, 0, count)

A = [1, 2, 3, 4, 5]
B = 1
obj = Solution()
obj.allIndices(A,B)