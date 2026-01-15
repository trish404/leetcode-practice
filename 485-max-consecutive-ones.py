class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr = 0
        max_ones = 0

        for n in nums:
            if n == 1:
                curr += 1
                max_ones = max(max_ones, curr)
            else:
                curr = 0

        return max_ones
