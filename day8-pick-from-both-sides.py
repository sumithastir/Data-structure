'''
Problem Description
You are given an integer array A of size N.

You have to perform B operations. In one operation, you can remove either the leftmost or the rightmost element of the array A.

Find and return the maximum possible sum of the B elements that were removed after the B operations.

NOTE: Suppose B = 3, and array A contains 10 elements, then you can:

Remove 3 elements from front and 0 elements from the back, OR
Remove 2 elements from front and 1 element from the back, OR
Remove 1 element from front and 2 elements from the back, OR
Remove 0 elements from front and 3 elements from the back.


Problem Constraints
1 <= N <= 105

1 <= B <= N

-103 <= A[i] <= 103



Input Format
First argument is an integer array A.

Second argument is an integer B.



Output Format
Return an integer denoting the maximum possible sum of elements you removed.



Example Input
Input 1:

 A = [5, -2, 3 , 1, 2]
 B = 3
Input 2:

 A = [ 2, 3, -1, 4, 2, 1 ]
 B = 4


Example Output
Output 1:

 8
Output 2:

 9


Example Explanation
Explanation 1:

 Remove element 5 from front and element (1, 2) from back so we get 5 + 1 + 2 = 8
Explanation 2:

 Remove the first element and the last 3 elements. So we get 2 + 4 + 2 + 1 = 9
'''


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer

    #
    #     Approach using Prefix and Suffix Sums:

    # Maintain two arrays prefix[i] and suffix[i] where prefix[i] denotes sum of elements from index [0,i] and suffix[i] denotes sum of elements from index [i,N-1].

    # Now iterate from left and one by one pick elements from left for example: if you pick ‘a’ elements from left and remaining ‘k-a’ elements from right.
    # So the sum in this case will be prefix[a-1] + suffix[n-(k-a)]

    # Maintain the maximum among all and return it.

    # Time Complexity: O(N)
    # Space Complexity: O(N)

    # where N is number of elements in array A

    # Bonus: Try solving it in O(1) space.

    def solve(self, A, B):
        prefix = [A[0]]
        N = len(A)
        for i in range(1, N):
            prefix.append(A[i] + prefix[i - 1])

        suffix = [0] * N

        suffix[N - 1] = A[N - 1]
        for i in range(N - 2, -1, -1):
            suffix[i] = A[i] + suffix[i + 1]

        i = B
        j = 0
        li = []
        while (i >= 0) and (j <= B):
            if i == B:
                li.append(prefix[B - 1])
            elif j == B:
                li.append(suffix[len(suffix) - B])
                break
            else:
                sub_sum = prefix[i - 1] + suffix[len(suffix) - j]
                li.append(sub_sum)
            i -= 1
            j += 1
        return max(li)

# Function Call
A = [5, -2, 3 , 1, 2]
B = 3

obj = Solution()
res = obj.solve(A, B)
print(res)