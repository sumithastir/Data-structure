'''
Problem Description
You are given an array A. Print the elements of the array using recursion.

NOTE :
You are required to not use any loops, You can create new functions.
Don't change the signature of the function PrintArray.
Print a new empty line after printing the output.

Problem Constraints
1 <= | A | <= 100
-1000 <= A[i] <= 1000

Input Format
One line containing the array A

Output Format
Print the elements of the array in the sequential order.

Example Input
Input 1 :
A = [6, -2, 5, 3]
Input 2 :
A = [1]


Example Output
Output 1 :
6 -2 5 3
Output 2 :
1

Example Explanation
Print the elements in their order.
'''

class Solution:
    def printArr(self, A, idx):
        if idx == len(A):
            return
        print(A[idx], end=" ")
        self.printArr(A, idx+1)

    # @param A : list of integers
    def PrintArray(self, A):
        self.printArr(A, 0)
        print()


A = [6, -2, 5, 3]
obj = Solution()
obj.PrintArray(A)