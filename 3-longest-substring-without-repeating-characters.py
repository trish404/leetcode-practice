class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        last_id = {}
        left = 0
        best = 0
        for right, char in enumerate(s):
            if char in last_id and last_id[char] >= left:
                left = last_id[char] + 1
            last_id[char] = right
            best = max(best, right-left+1)
        
        return best

        
