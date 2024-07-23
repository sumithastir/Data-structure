'''
Problems Statement:
Given an array of size N, find the majority element. The majority element is the element that appears more than floor(n/2) times.
You may assume that the array is non-empty and the majority element always exists in the array.

Problem Constraints:
1 <= N <= 5*105
1 <= num[i] <= 109

Input Format:
Only argument is an integer array.

Output Format:
Return an integer.

Example input:

Input 1:
[2, 1, 2]
Input 2:
[1, 1, 1]


Example Output
Input 1:
2
Input 2:
1

Example Explanation
For Input 1:
2 occurs 2 times which is greater than 3/2.
For Input 2:
 1 is the only element in the array, so it is majority

'''

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        N = len(A)
        freq = 1
        majority = A[0]
        for i in range(1, N):
            if freq == 0:
                freq = 1
                majority = A[i]
            elif A[i] == majority:
                freq+=1
            else:
                freq -=1
        return majority

A = [2, 1, 2]
obj = Solution()
res = obj.majorityElement(A)
print(res)

