class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        x = set(nums)
        return not (len(x) == len(nums))
        
