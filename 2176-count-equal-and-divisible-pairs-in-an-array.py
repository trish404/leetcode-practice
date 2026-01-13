class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        if len(set(nums)) == len(nums):
            return 0
        
        n = len(nums)
        tot = 0
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] == nums[j]:
                    a = i*j
                    if a%k == 0:
                        tot += 1
        return tot
