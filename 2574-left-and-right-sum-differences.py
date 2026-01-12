class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        leftSum = [0] * n
        rightSum = [0] * n
        leftSum[0] = 0
        rightSum[-1] = 0
        for i in range(1, n):
            j = n - i
            leftSum[i] = leftSum[i-1] + nums[i-1]
        
        for i in range(n-2, -1, -1):
            rightSum[i] = rightSum[i+1] + nums[i+1]
        res = []
        for i in range(n):
            res.append(abs(leftSum[i]-rightSum[i]))
        
        return res
