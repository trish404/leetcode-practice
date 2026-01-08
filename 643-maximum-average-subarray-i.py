class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        firstwindow = sum(nums[:k])
        best = firstwindow/float(k)

        for i in range(k, len(nums)):
            firstwindow += nums[i]
            firstwindow -= nums[i-k]

            best = max(best, firstwindow / float(k))
        
        return best

