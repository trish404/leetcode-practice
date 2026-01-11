class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set(nums)
        long = 0

        for x in s:
            if x-1 not in s:
                y = x
                while y in s:
                    y += 1
                long = max(long, y-x)
        
        return long
            
