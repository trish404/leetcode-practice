class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        k = s.strip().split(" ")
        l = len(k[-1])
        return l
        
