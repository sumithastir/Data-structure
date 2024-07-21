'''
Problem Description
You are given an integer array A. You have to find the second largest element/value in the array or report that no such element exists.


Problem Constraints
1 <= |A| <= 105

0 <= A[i] <= 109



Input Format
The first argument is an integer array A.



Output Format
Return the second largest element. If no such element exist then return -1.



Example Input
Input 1:

 A = [2, 1, 2]
Input 2:

 A = [2]


Example Output
Output 1:

 1
Output 2:

 -1


Example Explanation
Explanation 1:

 First largest element = 2
 Second largest element = 1
Explanation 2:

 There is no second largest element in the array.
'''
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        largest = second_largest = -1
        for a in A:
            if a > largest:
                second_largest = largest
                largest = a
            elif a > second_largest and a < largest:
                second_largest = a
        return second_largest


# Function Call
A = [2, 1, 2]

obj = Solution()
res = obj.solve(A)
print(res)