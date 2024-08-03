'''
Problem Description
You have a set of non-overlapping intervals. You are given a new interval [start, end],
insert this new interval into the set of intervals (merge if necessary).
You may assume that the intervals were initially sorted according to their start times.

Problem Constraints
0 <= |intervals| <= 105

Input Format
First argument is the vector of intervals

second argument is the new interval to be merged

Output Format
Return the vector of intervals after merging

Example Input
Input 1:

Given intervals [1, 3], [6, 9] insert and merge [2, 5] .
Input 2:

Given intervals [1, 3], [6, 9] insert and merge [2, 6] .


Example Output
Output 1:

 [ [1, 5], [6, 9] ]
Output 2:

 [ [1, 9] ]

Example Explanation
Explanation 1:

(2,5) does not completely merge the given intervals
Explanation 2:

(2,6) completely merges the given intervals
'''


class Solution:
    # @param A : list of list of integers
    # @param B : list of integers
    # @return a list of list of integers
    def insert(self, A, B):
        N = len(A)
        l = B[0]
        r = B[1]
        ans = []
        for i in range(N):
            if A[i][1] < l:
                ans.append(A[i])
            elif A[i][0] > r:
                ans.append([l, r])
                while i < N:
                    ans.append(A[i])
                    i += 1
                return ans
            else:
                l = min(l, A[i][0])
                r = max(r, A[i][1])

        ans.append([l, r])
        return ans



A = [[1, 3], [6, 9]]
B = [2, 5]
obj = Solution()
obj.insert(A,B)