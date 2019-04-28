'''
5. Longest Palindromic Substring
Medium

3405

328

Favorite

Share
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
'''


'''
the key is to find the dp solution

the shared dp solution
'''
class Solution:
    def longestPalindrome(self, s):
        dp = [[0]*len(s) for i in range(len(s))]
        ans = ""
        max_length = 0
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and (j-i<3 or dp[i+1][j-1]==1):
                    dp[i][j] = 1
                    if ans == "" or max_length < j-i+1:
                        ans = s[i:j+1]
                        max_length = j-i+1
        return ans

    '''
    或者直接利用回文串进行搜索扩展
    '''

    def solution2(self, s):
        if not s:
            return ""
        res = s[0]
        for i in range(0, len(s)-1):
            # for each point, two kind palindromes 
            l, r = i, i
            while l >= 0 and r<=len(s)-1 and s[l]==s[r]:
                l -= 1
                r += 1
            if len(s[l+1:r])>len(res):
                res = s[l+1:r]
            l, r = i, i+1
            while l>=0 and r <= (len(s)-1) and s[l]==s[r]:
                l -= 1
                r += 1
            if len(s[l+1:r]) > len(res):
                res = s[l+1:r]
        return res