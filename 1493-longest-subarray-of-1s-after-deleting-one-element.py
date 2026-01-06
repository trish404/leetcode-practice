class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        [0,1,1,1,0,1,1,0,1]
        maxl = 0
        start = 0 
        zero = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                start = zero + 1
                zero = i 
            maxl = max(maxl, i - start)
        
        return maxl 


        
