class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        res = 0
        for i in range(n):
            if nums[i] < k:
                res += 1
        
        return res
