class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        nums = [0] * n 
        nums[0] = start
        res = start
        for i in range(1, n):
            nums[i] = start + 2 * i
            res ^= nums[i]
        return res
