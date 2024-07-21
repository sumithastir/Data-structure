'''
Problem Description

Misha likes finding all Subarrays of an Array. Now she gives you an array A of N elements and told you to find the number of subarrays of A, that have unique elements.

Since the number of subarrays could be large, return value % 109 +7.



Problem Constraints

1 <= N <= 105

1 <= A[i] <= 106



Input Format

The only argument given is an Array A, having N integers.



Output Format

Return the number of subarrays of A, that have unique elements.



Example Input

Input 1:

 A = [1, 1, 3]
Input 2:

 A = [2, 1, 2]


Example Output

Output 1:

 4
Output 1:

 5


Example Explanation

Explanation 1:

 Subarrays of A that have unique elements only:
 [1], [1], [1, 3], [3]
Explanation 2:

 Subarrays of A that have unique elements only:
 [2], [1], [2, 1], [1, 2], [2]
'''


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        # Optimal Approach
        Mod = 1000000007
        N = len(A)
        l = 0
        r = 0
        ans = 0
        s = set()
        while r < N:
            if A[r] in s:
                s.remove(A[l])
                l += 1
            else:
                s.add(A[r])
                ans += r - l + 1
                r += 1
        return ans % Mod

        # N=len(A)
        # count=0
        # s=set()
        # l,r=0,0
        # mod=10**9+7
        # while r<N:
        #     if A[r] in s:
        #         s.remove(A[l])
        #         l+=1
        #     else:
        #         s.add(A[r])
        #         count+=(r-l+1)%mod
        #         r+=1

        # return count%mod

        # Brute Force
        # N = len(A)
        # res = []
        # for si in range(0, N):
        #     for ei in range(si, N):

        #         re = []
        #         isappend = True
        #         for k in range(si,ei+1):
        #             if A[k] not in re:
        #                 re.append(A[k])
        #             else:
        #                 re = []
        #                 isappend = False
        #         if isappend:
        #             res.append(re)

        # return len(res)


# Function Call
A = [1, 1, 3]

obj = Solution()
res = obj.solve(A)
print(res)