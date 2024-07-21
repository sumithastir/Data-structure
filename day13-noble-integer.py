'''
Problem Description
Given an integer array A, find if an integer p exists in the array such that the number of integers greater than p in the array equals p.



Problem Constraints
1 <= |A| <= 2*105
-108 <= A[i] <= 108


Input Format
First and only argument is an integer array A.



Output Format
Return 1 if any such integer p is present else, return -1.



Example Input
Input 1:

 A = [3, 2, 1, 3]
Input 2:

 A = [1, 1, 3, 3]


Example Output
Output 1:

 1
Output 2:

 -1


Example Explanation
Explanation 1:

 For integer 2, there are 2 greater elements in the array..
Explanation 2:

 There exist no integer satisfying the required conditions.
'''


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        N = len(A)  # such as 9 for [1,2,7,0,9,3,6,0,6]

        count_larger = 0
        A.sort()  # [0,0,1,2,3,6,6,7,9]

        if A[N - 1] == 0:
            return 1
        for i in range(N - 2, -1, -1):
            # print(i)
            if A[i] != A[i + 1]:
                count_larger = (N - 1) - i
            if A[i] == count_larger:
                return 1

        return -1


# Function Call
A = [3, 2, 1, 3]

obj = Solution()
res = obj.solve(A)
print(res)