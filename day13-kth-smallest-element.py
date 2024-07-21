'''
Problem Description
Find the Bth smallest element in given array A .

NOTE: Users should try to solve it in less than equal to B swaps.



Problem Constraints
1 <= |A| <= 100000

1 <= B <= min(|A|, 500)

1 <= A[i] <= 109



Input Format
The first argument is an integer array A.

The second argument is integer B.



Output Format
Return the Bth smallest element in given array.



Example Input
Input 1:

A = [2, 1, 4, 3, 2]
B = 3
Input 2:

A = [1, 2]
B = 2


Example Output
Output 1:

 2
Output 2:

 2


Example Explanation
Explanation 1:

 3rd element after sorting is 2.
Explanation 2:

 2nd element after sorting is 2.
'''


class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, B):
        N = len(A)
        A = list(A)

        for i in range(0, N):
            min_ele = A[i]
            min_idx = i
            for j in range(i + 1, N):
                if A[j] < min_ele:
                    min_ele = A[j]
                    min_idx = j
            temp = A[i]
            A[i] = A[min_idx]
            A[min_idx] = temp

            if i + 1 == B:
                return A[i]

# Function Call
A = [2, 1, 4, 3, 2]
B = 3

obj = Solution()
res = obj.kthsmallest(A, B)
print(res)