class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        tot = 0
        for i, ch in enumerate(s):
            val = 26 - (ord(ch) - ord('a'))
            tot += (val)*(i+1)

        
        return tot
