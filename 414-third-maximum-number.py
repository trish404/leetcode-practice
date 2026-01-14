class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        uniq = sorted(set(nums), reverse=True)
        return uniq[2] if len(uniq) >= 3 else uniq[0]
