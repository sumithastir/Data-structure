'''
Problem Description
Given an array A of N integers.
Count the number of elements that have at least 1 elements greater than itself.


Problem Constraints
1 <= N <= 105
1 <= A[i] <= 109


Input Format
First and only argument is an array of integers A.


Output Format
Return the count of elements.


Example Input
Input 1:
A = [3, 1, 2]
Input 2:
A = [5, 5, 3]


Example Output
Output 1:
2
Output 2:
1


Example Explanation
Explanation 1:
The elements that have at least 1 element greater than itself are 1 and 2
Explanation 2:
The elements that have at least 1 element greater than itself is 3
'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        max_element = max(A)
        count = 0
        for a in A:
            if a < max_element:
                count+=1
        return count

# Function Call
A = [3, 1, 2]

obj = Solution()
res = obj.solve(A)
print(res)