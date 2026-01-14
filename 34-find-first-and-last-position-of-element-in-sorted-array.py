class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        res = []
        for i, n in enumerate(nums):
            if n == target:
                res.append(i)
        if res:
            return[min(res), max(res)]
        else:
            return [-1, -1]
