'''
Problem Description
Given an array A and an integer B. A pair(i, j) in the array is a good pair if i != j and (A[i] + A[j] == B). Check if any good pair exist or not.



Problem Constraints
1 <= A.size() <= 10^4

1 <= A[i] <= 10^9

1 <= B <= 10^9



Input Format
First argument is an integer array A.

Second argument is an integer B.



Output Format
Return 1 if good pair exist otherwise return 0.



Example Input
Input 1:

A = [1,2,3,4]
B = 7
Input 2:

A = [1,2,4]
B = 4
Input 3:

A = [1,2,2]
B = 4


Example Output
Output 1:

1
Output 2:

0
Output 3:

1


Example Explanation
Explanation 1:

 (i,j) = (3,4)
Explanation 2:

No pair has sum equal to 4.
Explanation 3:

 (i,j) = (2,3)
'''
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        i = 0
        len_of_arr = len(A)
        while i < len_of_arr:
            j = i+1
            while j <  len_of_arr:
                if A[i] + A[j] == B:
                    return 1
                j+=1
            i+=1
        return 0

# Function Call
A = [1,2,3,4]
B = 7

obj = Solution()
res = obj.solve(A, B)
print(res)