class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        tot = 0
        for x in nums:
            s = str(x)
            mx = max(s)
            tot += int(mx * len(s))
        
        return tot
