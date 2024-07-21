'''
Problem Description
Given an array, arr[] of size N, the task is to find the count of array indices such that removing an element from these indices makes the sum of even-indexed and odd-indexed array elements equal.



Problem Constraints
1 <= N <= 105
-105 <= A[i] <= 105
Sum of all elements of A <= 109


Input Format
First argument contains an array A of integers of size N


Output Format
Return the count of array indices such that removing an element from these indices makes the sum of even-indexed and odd-indexed array elements equal.



Example Input
Input 1:
A = [2, 1, 6, 4]
Input 2:

A = [1, 1, 1]


Example Output
Output 1:
1
Output 2:

3


Example Explanation
Explanation 1:
Removing arr[1] from the array modifies arr[] to { 2, 6, 4 } such that, arr[0] + arr[2] = arr[1].
Therefore, the required output is 1.
Explanation 2:

Removing arr[0] from the given array modifies arr[] to { 1, 1 } such that arr[0] = arr[1]
Removing arr[1] from the given array modifies arr[] to { 1, 1 } such that arr[0] = arr[1]
Removing arr[2] from the given array modifies arr[] to { 1, 1 } such that arr[0] = arr[1]
Therefore, the required output is 3.
'''


class Solution:
    # @param A : list of integers
    # @return an integer
    def pfeven(self, A):
        peven = [A[0]]
        N = len(A)
        for i in range(1, N):
            if (i % 2 == 0):
                peven.append(peven[i - 1] + A[i])
            else:
                peven.append(peven[i - 1])
        return peven

    def pfodd(self, A):
        podd = [0]
        N = len(A)
        for i in range(1, N):
            if (i % 2 == 1):
                podd.append(podd[i - 1] + A[i])
            else:
                podd.append(podd[i - 1])
        return podd

    def solve(self, A):
        count = 0
        N = len(A)
        pfodd = self.pfodd(A)
        pfeven = self.pfeven(A)

        if pfodd[N - 1] - pfodd[0] == pfeven[N - 1] - pfeven[0]:
            count += 1

        for i in range(1, N):
            se = pfeven[i - 1] + pfodd[N - 1] - pfodd[i]

            so = pfodd[i - 1] + pfeven[N - 1] - pfeven[i]
            if se == so:
                count += 1

        return count

# Function Call
A = [2, 1, 6, 4]

obj = Solution()
res = obj.solve(A)
print(res)