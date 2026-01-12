class Solution(object):
    def mirrorDistance(self, n):
        """
        :type n: int
        :rtype: int
        """
        rev = str(n)
        
        return abs(n - int(rev[::-1]))
