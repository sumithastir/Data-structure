'''
Problems Statement:
Given a number A, find if it is COLORFUL number or not.If number A is a COLORFUL number return 1 else, return 0.

What is a COLORFUL Number: A number can be broken into different consecutive sequence of digits.
The number 3245 can be broken into sequences like 3, 2, 4, 5, 32, 24, 45, 324, 245 and 3245.
This number is a COLORFUL number, since the product of every consecutive sequence of digits is different



Problem Constraints:
1 <= A <= 2 * 10^9

Input Format:
The first and only argument is an integer A.

Output Format:
Return 1 if integer A is COLORFUL else return 0.

Example input:
Input 1:
 A = 23
Input 2:
 A = 236


Example Output
Output 1:
1
Output 2:
0

Example Explanation
Explanation 1:

 Possible Sub-sequences: [2, 3, 23] where
 2 -> 2
 3 -> 3
 23 -> 6  (product of digits)
 This number is a COLORFUL number since product of every digit of a sub-sequence are different.
 
Explanation 2:

 Possible Sub-sequences: [2, 3, 6, 23, 36, 236] where
 2 -> 2
 3 -> 3
 6 -> 6
 23 -> 6  (product of digits)
 36 -> 18  (product of digits)
 236 -> 36  (product of digits)
 This number is not a COLORFUL number since the product sequence 23  and sequence 6 is same.

'''


class Solution:
    # @param A : integer
    # @return an integer
    def colorful(self, A):
        numbers = []

        while A != 0:
            num = A % 10
            numbers.append(num)
            A = A // 10

        # simply reverse the List
        N = len(numbers)
        l = 0
        r = N - 1
        while l < r:
            numbers[l], numbers[r] = numbers[r], numbers[l]
            l += 1
            r -= 1
        # print(numbers)
        unique_list = []
        for i in range(0, N):
            prod = 1
            for j in range(i, N):
                prod = prod * numbers[j]
                if prod in unique_list:
                    return 0
                unique_list.append(prod)

                # print(unique_list)
        return 1


A = 23

obj = Solution()
res = obj.colorful(A)
print(res)



