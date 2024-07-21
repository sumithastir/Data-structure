'''
Problem Description
You are given an array A of N integers.
Return a 2D array consisting of all the subarrays of the array

Note : The order of the subarrays in the resulting 2D array does not matter.


Problem Constraints
1 <= N <= 100
1 <= A[i] <= 105


Input Format
First argument A is an array of integers.


Output Format
Return a 2D array of integers in any order.


Example Input
Input 1:
A = [1, 2, 3]
Input 2:
A = [5, 2, 1, 4]


Example Output
Output 1:
[[1], [1, 2], [1, 2, 3], [2], [2, 3], [3]]
Output 2:
[[1 ], [1 4 ], [2 ], [2 1 ], [2 1 4 ], [4 ], [5 ], [5 2 ], [5 2 1 ], [5 2 1 4 ] ]


Example Explanation
For Input 1:
All the subarrays of the array are returned. There are a total of 6 subarrays.
For Input 2:
All the subarrays of the array are returned. There are a total of 10 subarrays.
'''


class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def solve(self, A):
        N = len(A)
        res = []
        for si in range(0, N):
            for ei in range(si, N):
                res.append(self.printSubArray(A, si, ei))
        return res

    def printSubArray(self, arr, si, ei):
        re = []
        for k in range(si, ei + 1):
            re.append(arr[k])
        return re

# Function Call
A = [1, 2, 3]

obj = Solution()
res = obj.solve(A)
print(res)