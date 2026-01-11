class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x
        
        l = 1
        r = x//2
        res = 0

        while l <= r:
            m = (l+r) // 2
            if m * m <= x:
                res = m
                l = m + 1
            else:
                r = m - 1
        
        return res
        
