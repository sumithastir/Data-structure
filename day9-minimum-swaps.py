'''
Problem Description

Given an array of integers A and an integer B, find and return the minimum number of swaps required to bring all the numbers less than or equal to B together.

Note: It is possible to swap any two elements, not necessarily consecutive.



Problem Constraints

1 <= length of the array <= 100000
-109 <= A[i], B <= 109



Input Format

The first argument given is the integer array A.
The second argument given is the integer B.



Output Format

Return the minimum number of swaps.



Example Input

Input 1:

 A = [1, 12, 10, 3, 14, 10, 5]
 B = 8
Input 2:

 A = [5, 17, 100, 11]
 B = 20


Example Output

Output 1:

 2
Output 2:

 1


Example Explanation

Explanation 1:

 A = [1, 12, 10, 3, 14, 10, 5]
 After swapping  12 and 3, A => [1, 3, 10, 12, 14, 10, 5].
 After swapping  the first occurence of 10 and 5, A => [1, 3, 5, 12, 14, 10, 10].
 Now, all elements less than or equal to 8 are together.
Explanation 2:

 A = [5, 17, 100, 11]
 After swapping 100 and 11, A => [5, 17, 11, 100].
 Now, all elements less than or equal to 20 are together.

'''


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        N = len(A)
        # First of we find the number of element Less than of equal to B
        no_of_ele_less_than_B = 0
        for i in range(0, N):
            if A[i] <= B:
                no_of_ele_less_than_B += 1

        # Use C just for simplification
        C = no_of_ele_less_than_B
        # Calculate curr_swap -> no of element greater than B , we need to swap for them
        curr_swap = 0
        for i in range(0, C):
            if A[i] > B:
                curr_swap += 1
        # intialize min_swap with curr_swap
        min_swap = curr_swap

        # use sliding window to add one element and remove one from starting and calculate swap again
        for i in range(C, N):
            if A[i] > B:
                curr_swap += 1
            if A[i - C] > B:
                curr_swap -= 1
            if curr_swap < min_swap:
                min_swap = curr_swap
        return min_swap

        # l = 0
        # N = len(A)
        # r = N - 1
        # swap = 0
        # while l < r:
        #     while A[l] <= B:
        #         l+=1
        #     while A[r] > B:
        #         r-=1
        #     if l < r:
        #         print(A[l])

        #         A[l], A[r] = A[r], A[l]
        #         swap +=1
        #         l+=1
        #         r-=1

        # return swap


# Function Call
A = [1, 12, 10, 3, 14, 10, 5]
B = 8

obj = Solution()
res = obj.solve(A, B)
print(res)