class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        far = 0
        last = len(nums) - 1
        for i in range(len(nums)):
            if i > far:
                return False
            far = max(far, i + nums[i])
            if far >= last:
                return True
        
        return True
