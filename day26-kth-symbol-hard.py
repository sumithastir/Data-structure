'''
Problem Description
On the first row, we write a 0. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

Given row number A and index B, return the Bth indexed symbol in row A. (The values of B are 0-indexed.).

Problem Constraints
1 <= A <= 105

0 <= B <= min(2A - 1 - 1 , 1018)

Input Format
First argument is an integer A.

Second argument is an integer B.

Output Format
Return an integer denoting the Bth indexed symbol in row A.

Example Input
Input 1:

 A = 3
 B = 0
Input 2:

 A = 4
 B = 4

Example Output
Output 1:

 0
Output 2:

 1

Example Explanation
Explanation 1:

 Row 1: 0
 Row 2: 01
 Row 3: 0110
Explanation 2:

 Row 1: 0
 Row 2: 01
 Row 3: 0110
 Row 4: 01101001
'''


class Solution:
    '''
    The required solution for finding the Bth indexed symbol in the Ath row of a sequence relies
    on understanding the pattern of sequence formation and the parent-child relationship between
    symbols in consecutive rows. Starting with 0 on the first row, each subsequent row is generated
    by replacing 0 with 01 and 1 with 10.

    The key observation is that any symbol at index B in row A
    is derived from the symbol at index B//2 in row A-1. The recursive approach leverages this by
    determining the symbol at B//2 in the previous row and then using the parity of B to decide the
    current symbol. If B is even, the symbol remains the same as the parent's, and if odd, it is the
    opposite. This approach avoids generating entire rows, making it efficient with a time complexity of O(log(B)).
    '''

    # @param A : integer
    # @param B : long
    # @return an integer
    def solve(self, A, B):
        sys.setrecursionlimit(10 ** 5)
        ans = self.findIndexValue(A, B)
        return ans

    def findIndexValue(self, A, B):
        if A == 1:
            return 0
        if B in (0, 1):
            return B
        num = self.findIndexValue(A - 1, B // 2)
        if B % 2 == 0:
            return num
        return num ^ 1


A = 3
B = 0

obj = Solution()
obj.findIndexValue(A, B)