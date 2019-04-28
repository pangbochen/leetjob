'''
7. Reverse Integer
Easy

2077

3123

Favorite

Share
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
'''
'''
the key solution for the recursive method
'''

class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        INT_MAX = (2**32-1)//10
        INT_MIN = (-2**32)//10
        while x!=0:
            pop = x%10
            x = x//10
            # add the checking rules
            if rev > INT_MAX or (rev==INT_MAX and pop>7):
                return 0
            if rev < INT_MIN or (rev==INT_MIN and pop<-8):
                return 0
            rev = rev*10+pop
        return rev
    
    # the above solution will time-exceeded limited
    # the log solution
    def reverse(self, num):
        negativeFlag = False
        if num < 0:
            negativeFlag = True
            num = -num
        prev_rev_num = 0
        rev_num = 0

        while num!=0:
            curr_digit = num % 10
            rev_num = (rev_num*10)+curr_digit
            if rev_num>2147483647 or rev_num<= -2147483648:
                rev_num = 0
            if (rev_num-curr_digit)//10 != prev_rev_num:
                return 0
            prev_rev_num = rev_num
            num = num // 10
        
        return -rev_num if negativeFlag else rev_num
