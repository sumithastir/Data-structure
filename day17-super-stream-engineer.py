'''
Problems Statement:
You've just been hired as a network engineer at SuperStream, a leading video streaming service. One of your first tasks
is to optimize the number of video data packets sent to users based on thier internet connectivity.

when a user hits "play", video data is transmitted in packets. if their device acknowledges these packets quickly, it means they have a
strong connection and can receive more packets simultaneously for smoother streaming. If acknowledgements lag, fewer packets
should be sent to prevent buffering.

Given an array A, where each entry represents the acknowledgement time (in milliseconds) for individual packets,
and two integers B and C, can your determine if there's continuous sequence of B packtes with an average acknowledgement time
less than or equal to C milliseconds?
If so, it's a green signal (integer 1) to send more packets. Ohterwise, it's time to throttle back (integer 0)

Note: For average, take the floor of (sum/total number of elements).

Problem Constraints:
1 <= N <= 10^5
1 <= A[i] <= 10^9
1 <= B <= N
1 <= C <= 10^9

Input Format:
First argument A, is an array of integers
The remaining arguments B and C are integers

Output Format:
Return 1 if such an subarray exist and 0 otherwise

Example input:
Input 1:
A = [30, 25, 40, 35, 20, 45, 50, 55, 22, 18, 15]
B = 3
C = 30

Input 1:
A = [4, 2, 2, 5, 1]
B = 4
C = 1

Example Output:
Output1: 1
Output2: 0

'''

class Solution:
    def solve(self, A, B, C):
        N = len(A)
        # if len(B) > len(A) then return 0.
        if B > len(A):
            return 0

        curr_sum = 0
        for i in range(0, B):
            curr_sum += A[i]
        if curr_sum // B <= C:
            return 1

        for i in range(B, N):
            curr_sum = curr_sum + A[i] - A[i-B]
            if curr_sum // B <= C:
                return 1
        return 0




print("Test Example 1")
A = [30, 25, 40, 35, 20, 45, 50, 55, 22, 18, 15]
B = 3
C = 30
S = Solution()
print(S.solve(A, B, C))

print("Test Example 2")
A = [4, 2, 2, 5, 1]
B = 4
C = 1

S = Solution()
print(S.solve(A, B, C))

print("Test Example 3")
A = [4, 2, 2, 5, 1]
B = 6
C = 1

S = Solution()
print(S.solve(A, B, C))

