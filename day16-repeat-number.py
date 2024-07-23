'''
Problems Statement:
You're given a read-only array of N integers. Find out if any integer occurs more than N/3 times in the array in linear time and constant additional space.
If so, return the integer. If not, return -1.

If there are multiple solutions, return any one.

Note: Read-only array means that the input array should not be modified in the process of solving the problem



Problem Constraints:
1 <= N <= 7*10^5
1 <= A[i] <= 10^9

Input Format:
The only argument is an integer array A.

Output Format:
Return an integer.

Example input:
Input 1:
[1 2 3 1 1]
Input 2:
[1 2 3]


Example Output
Output 1:
1
Output 2:
-1

Example Explanation
Explanation 1:
1 occurs 3 times which is more than 5/3 times.
Explanation 2:
No element occurs more than 3 / 3 = 1 times in the array.

'''

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        majority1 = -1
        majority2 = -1
        freq1 = 0
        freq2 = 0
        N = len(A)

        for i in range(0, N):
            if majority1 == A[i]:
                freq1 +=1
            elif majority2 == A[i]:
                freq2 +=1
            elif freq1 == 0:
                majority1 = A[i]
                freq1+=1
            elif freq2 == 0:
                majority2 = A[i]
                freq2+=1
            else:
                freq1-=1
                freq2-=1
        c1 = majority1
        c2 = majority2
        freq1 = 0
        freq2 = 0
        for i in range(0, N):
            if A[i] == c1:
                freq1 +=1
            if A[i] == c2:
                freq2 +=1

        if freq1 > N/3:
            return c1
        elif freq2 > N/3:
            return c2
        else:
            return -1


A = [1,2, 3, 1, 1]
obj = Solution()
res = obj.repeatedNumber(A)
print(res)

