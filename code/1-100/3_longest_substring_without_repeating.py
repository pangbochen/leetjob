'''
3. Longest Substring Without Repeating Characters
Medium

5278

280

Favorite

Share
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution:
    def lengthOfLongestSubString(self, s):
        n, ans = len(s), 0
        char_index = {}
        i, j = 0, 0
        while j<n:
            if s[j] in char_index:
                i = max(char_index[s[j]]+1, i)
            ans = max(ans, j-i+1)
            char_index[s[j]] = j # update the char_index
            j += 1
        return ans