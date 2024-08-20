'''
Problem Description
Given an integer array A of size N, find the first repeating element in it.

We need to find the element that occurs more than once and whose index of the first occurrence is the smallest.

If there is no repeating element, return -1.


Problem Constraints
1 <= N <= 105

1 <= A[i] <= 109

Input Format
The first and only argument is an integer array A of size N.


Output Format
Return an integer denoting the first repeating element.


Example Input
Input 1:

 A = [10, 5, 3, 4, 3, 5, 6]
Input 2:

 A = [6, 10, 5, 4, 9, 120]


Example Output
Output 1:

 5
Output 2:

 -1


Example Explanation
Explanation 1:

 5 is the first element that repeats
Explanation 2:

 There is no repeating element, output -1

'''


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        # both technique are good

        n = len(A)
        # Initialize index of first repeating element
        mini = -1

        # Creates an empty hashset named ump
        ump = {}

        # Traverse the input array from right to left
        for i in range(n - 1, -1, -1):
            # If element is already in hash set, update min
            if (ump.get(A[i]) != None):
                mini = i
            else:  # Else add element to hash set
                ump[A[i]] = 1

        if (mini == -1):
            return mini

        return A[mini]

        # Awnser share in Class.
        # first find frequency of each element an store in Hashmap or dictionary
        # then go to each element of A and find first that have freq count greater than 1

        # freq_map = {}
        # for a in A:
        #     if a in freq_map:
        #         freq_map[a] += 1
        #     else:
        #         freq_map[a] = 1
        # for k in A:
        #     if freq_map[k] > 1:
        #         return k
        # return -1


A = [10, 5, 3, 4, 3, 5, 6]

obj = Solution()
obj.solve(A)