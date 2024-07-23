'''
Problems Statement:
You are given an array A of N elements. Find the number of triplets i,j and k such that i<j<k and A[i]<A[j]<A[k]

Problem Constraints:
1 <= N <= 10^3
1 <= A[i] <= 10^9

Input Format:
First argument A is an array of integers.

Output Format:
Return an integer.

Example input:
Input 1:
A = [1, 2, 4, 3]
Input 2:
A = [2, 1, 2, 3]


Example Output
Output 1:
2
Output 2:
1

Example Explanation
For Input 1:
The triplets that satisfy the conditions are [1, 2, 3] and [1, 2, 4].
For Input 2:

The triplet that satisfy the conditions is [1, 2, 3].

'''


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        cnt = 0
        N = len(A)
        for i in range(1, N - 1):
            # print(A[i])
            count_smaller = 0
            l = i - 1
            while l >= 0:
                if A[i] > A[l]:
                    count_smaller += 1
                l -= 1
            # print(count_smaller)
            count_greater = 0
            r = i + 1
            while r < N:
                if A[r] > A[i]:
                    count_greater += 1
                r += 1
            # print(count_greater)

            if count_greater > 0 and count_smaller > 0:
                cnt += (count_smaller * count_greater)
        return cnt

A = [1, 2, 4, 3]
obj = Solution()
res = obj.majorityElement(A)
print(res)