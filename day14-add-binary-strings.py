'''
Problem Description
Given two binary strings A and B. Return their sum (also a binary string).


Problem Constraints
1 <= length of A <= 105

1 <= length of B <= 105

A and B are binary strings



Input Format
The two argument A and B are binary strings.



Output Format
Return a binary string denoting the sum of A and B



Example Input
Input 1:
A = "100"
B = "11"
Input 2:
A = "110"
B = "10"


Example Output
Output 1:
"111"
Output 2:
"1000"


Example Explanation
For Input 1:
The sum of 100 and 11 is 111.
For Input 2:

The sum of 110 and 10 is 1000.
'''

class Solution:
	# @param A : string
	# @param B : string
	# @return a strings
    def addBinary(self, A, B):
        ans = 0
        power = 1
        carry = 0
        n1 = int(A)
        n2 = int(B)
        while (n1 > 0 or n2 > 0 or carry>0):
            l1 = n1 % 10
            l2 = n2 % 10
            # print(l1)
            # print(l2)
            n1 = n1//10
            n2 = n2//10
            current_sum = l1 + l2 + carry
            q = current_sum//2
            r = current_sum%2
            ans += r* power
            carry = q
            power *=10
        return ans

# Function Call
A = "100"
B = "11"
obj = Solution()
res = obj.addBinary(A, B)
print(res)