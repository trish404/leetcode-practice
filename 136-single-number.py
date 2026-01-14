from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x = Counter(nums)
        for n, f in x.items():
            if f == 1:
                return n
