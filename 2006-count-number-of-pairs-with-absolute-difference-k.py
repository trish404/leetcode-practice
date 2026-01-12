class Solution(object):
    def countKDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        opt = 0
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if abs(nums[i] - nums[j]) == k:
                    opt += 1
        return opt

