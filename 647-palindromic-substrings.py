class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                tmp = s[i:j+1]
                if tmp == tmp[::-1]:
                    counter += 1
        
        return counter
        
