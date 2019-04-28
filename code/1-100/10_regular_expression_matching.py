'''
10. Regular Expression Matching
Hard

2459

477

Favorite

Share
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
'''


class Solution:
    def isMatch(self, s, p):
        # the traditional dp solution
        '''
        1.s[i] == p[j] or p[j] == '.' dp[i][j] = dp[i-1][j-1]
        2.p[j] == '*'
            2.1 s[i] != p[j-1] and p[j-1]!='.': dp[i][j] = dp[i][j-2]
            2.2 else: 
        '''
        m, n = len(s), len(p)
        dp = collections.defaultdict(lambda : False)
        dp[-1,-1] = True

        for i in range(-1, m):
            for j in range(n):
                if i>=0 and s[i]==p[j] or p[j]=='.':
                    dp[i, j] = dp[i-1, j-1]
                if p[j] == '*':
                    if i == -1 or s[i]!=p[j-1] and p[j-1]!='.':
                        dp[i, j] = dp[i, j-2]
                    else:
                        dp[i, j] = dp[i, j-1] or dp[i-1, j] or dp[i-1, j]
        return dp[m-1, n-1]
        