class Solution(object):
    def sumOfMultiples(self, n):
        """
        :type n: int
        :rtype: int
        """
        tot = 0
        for i in range(1, n+1):
            if i % 3 == 0:
                tot += i
            elif i % 5 == 0:
                tot += i
            elif i % 7 == 0:
                tot += i
            
        return tot
