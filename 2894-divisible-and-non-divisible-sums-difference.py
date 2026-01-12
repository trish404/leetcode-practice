class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        div = 0
        non = 0
        for i in range(n+1):
            if i % m == 0:
                div += i
            else:
                non += i
        return non - div 
