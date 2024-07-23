'''
Problems Statement:
Given a binary string A. It is allowed to do at most one swap between any 0 and 1.
Find and return the length of the longest consecutive 1’s that can be achieved.

Problem Constraints:
1 <= length of string <= 1000000
A contains only characters 0 and 1.

Input Format:
The only argument given is string A.

Output Format:
Return the length of the longest consecutive 1’s that can be achieved.

Example input:
Input 1:
    A = "111000"
Output 1:
    3

Input 2:
    A = "111011101"
Output 2:
    7

'''


class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        N = len(A)
        ans = 0
        totalones = 0
        for i in range(0, N):
            if int(A[i]) == 1:
                totalones += 1

        # print(totalones)
        if totalones == 0:
            return 0
        if totalones == N:
            return N

        for i in range(0, N):
            if int(A[i]) == 0:

                l = 0
                r = 0
                for j in range(i - 1, -1, -1):
                    if int(A[j]) == 1:
                        l += 1
                    else:
                        break
                for j in range(i + 1, N):
                    if int(A[j]) == 1:
                        r += 1
                    else:
                        break
                fact = l + r

                if l + r < totalones:
                    fact = l + r + 1
                ans = max(ans, fact)
        return ans

A = "111000"
obj = Solution()
res = obj.solve(A)
print(res)




