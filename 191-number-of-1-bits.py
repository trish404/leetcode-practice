from collections import Counter
class Solution:
    def hammingWeight(self, n: int) -> int:
        x = str(bin(n))[2:]
        y = Counter(x)
        return y['1']
