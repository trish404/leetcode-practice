class Solution(object):
    def transformArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        for i in range(len(nums)):
            nums[i] = nums[i] % 2
        nums.sort()
        return nums
