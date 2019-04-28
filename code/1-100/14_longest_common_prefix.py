'''
14. Longest Common Prefix
Easy

1292

1264

Favorite

Share
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # the brute method 
        # grab for each index 
        if not strs:
            return ''
        mins = min((strs))
        maxs = max((strs))
        pre = ''
        for i in range(min(len(mins), len(maxs))):
            if mins[i] == maxs[i]:
                pre = pre+mins[i]
            else:
                break
        return pre

    # the trie pyhton method
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        self.Trie_root = {} # creat Trie root
        
        for str in strs:
            self.insert(str)
        
        cur_node = self.Trie_root
        if None in cur_node or len(cur_node.keys()) > 1:
            return ""
        for i, c in enumerate(strs[0]):
            cur_node = cur_node[c]
            if None in  cur_node or len(cur_node.keys())>1:
                return strs[0][:i+1]
    
    def insert(self, word):
        """
        Inserts a word into trie
        while space cost is too large
        """
        cur_node = self.Trie_root
        for w in word:
            if w not in cur_node:
                cur_node[w] = {}
            cur_node = cur_node[w]
        cur_node[None] = True


    
    # more python style solution
    # zip and set method
    # same with the brute solution 
    # with built-in zip to accelerate
    def longestCommonPrefix(self, strs: List[str]) -> str:
        out = []
        for k in ({*k} for x in zip(*strs)):
            if len(k) > 1: 
                break
            out.append(k.pop())
        return ''.join(out)

    
    '''
    the horizontal scanning solution
    '''
    '''
    the divide and conquer solution
    space for O(mLogn)
    time for O(S)
    '''


    # the typical brute solution
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        strs.sort()
        common = strs[0]
        if not common:
            return ""
        length = len(common)
        for s in strs:

    # the optimized tire tree solution 
