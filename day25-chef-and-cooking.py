'''

The chef's goal is to determine the maximum possible sum of the weights of the strictly increasing subarray.
Can you assist the chef by writing a function that returns the maximum possible sum of an strictly increasing
subarray from the given array of ingredient weights

The array of ingredient weights is represented by the array A.

[5 5 7 2 1 3 4 6 2 9]


'''

class Solution():
    def solve(self, A):
        curr_sum = A[0]
        ans = A[0]
        N = len(A)
        for i in range(N):
            if A[i] > A[i-1]:
                curr_sum += A[i]
            else:
                curr_sum = A[i]
                ans = max(ans, curr_sum)

        return ans


A = [5, 5, 7, 2, 1, 3, 4, 6, 2, 9]
obj = Solution()
result = obj.solve(A)
print(result)
