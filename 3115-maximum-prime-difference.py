class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        def isprime(x: int) -> bool:
            if x < 2:
                return False
            for i in range(2, int(x**0.5) + 1):
                if x % i == 0:
                    return False
            return True

        l = []
        for i, n in enumerate(nums):
            if isprime(n):
                l.append(i)
        
        return abs(max(l)-min(l))
