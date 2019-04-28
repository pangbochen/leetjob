'''
9. Palindrome Number
Easy

1345

1262

Favorite

Share
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
'''

'''
the pyhton number solution
'''

class Solution:
    def isPalindrome(self, x):
        # x: int number
        if x < 0:
            return False
        else:
            res = 0
            tmp = x
            while tmp:
                res = res*10 + tmp%10
                tmp = tmp // 10
            return res == x
            