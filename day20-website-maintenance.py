'''
Problem Description
Scaler Academy, a leading ed-tech platform known for its comprehensive learning programs,
is planning to conduct maintenance on its website to enhance user experience and introduce new features.
To ensure the maintenance work does not disrupt the scheduled meets of various batches,
Scaler Academy aims to schedule this maintenance during the period of no user activity.

Given sorted intervals A on the active hours of multiple learners on the platform and
the scheduled meeting by [start, end], where time is denoted by numbers.
Your task is to analyze this data and identify the longest continuous period when no meetings are scheduled
before the end time B.
This identified time slot is crucial as it represents the best opportunity to perform website maintenance
with the least disruption to the scheduled meets of various batches.

Refer the Example Explanation for better understanding!

Problem Constraints
1 <= A.length <= 105
A[i].length == 2
0 <= A[i][0] < A[i][1] <= 105
A is sorted in non-decreasing order

Input Format
First Argument is a 2-D Integer Array A, of size Nx2.
Second Argument is an Integer B.

Output Format
Return an Integer, denoting the longest continuous period.

Example Input
Input 1:
A = [ [1, 3], [5, 8], [6, 7], [7, 9] ]
B = 12
Input 2:
A = [ [0, 5], [2, 7] ]
B = 7

Example Output
Output 1:
3
Output 2:
0

Example Explanation
Explanation 1:
Explanation
The longest continuous period when no meetings are scheduled is [9, 12].

Thus the answer is 3.
Explanation 2:
Explanation

There is No free hours.  Thus the answer is 0.

'''


class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def findLongestTime(self, A, B):
        N = len(A)
        merged_internal = []
        l = A[0][0]
        r = A[0][1]
        for i in range(1, N):
            if A[i][0] > r:
                merged_internal.append([l, r])
                l = A[i][0]
                r = A[i][1]
            else:
                r = max(r, A[i][1])

        merged_internal.append([l, r])
        # print(merged_internal)
        n = len(merged_internal)
        free_hours = 0
        for i in range(n):

            l = merged_internal[i][0]
            r = merged_internal[i][1]
            if i == 0:
                free_hours = l
            else:
                free_hours = max(free_hours, l - merged_internal[i - 1][1])

            if i == n - 1:
                free_hours = max(free_hours, B - r)

        return free_hours

A = [ [1, 3], [5, 8], [6, 7], [7, 9] ]
B = 12
obj = Solution()
obj.findLongestTime(A,B)