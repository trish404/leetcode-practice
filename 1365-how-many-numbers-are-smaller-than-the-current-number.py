class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = []
        for i in range(n):
            tot = 0
            for j in range(n):
                if i != j:
                    if nums[i] > nums[j]:
                        tot += 1
            res.append(tot)
        return res
