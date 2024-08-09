'''
Dr. Benjamin explained that the students' task was to analyze the array and determine the count of pairs
that satisfied a unique condition. The condition revolved around the XOR operation on the ith bit of the pair's
elements. The goal was to count the pairs for which the xor of the ith bit resulted in one.
You have to answer for Q queries given in array B, each query B[i] denotes the index for which you need to
find the count of pairs with xor of that index equals 1

A = [2,3,5,7]
B = [2]
'''


class Solution():
    def solve(self, A, B):
        b_len = len(B)
        N = len(A)
        result = []
        for i in range(b_len):
            set_bits = 0
            for j in range(N):
                if A[j] & (1<<B[i]) != 0:
                    set_bits +=1
            unset_bits = N - set_bits
            print(set_bits * unset_bits)
            result.append(set_bits * unset_bits)

        return result

A = [2,3,5,7]
B = [2]
obj = Solution()
result = obj.solve(A, B)
print(result)

