class Solution:
    def alternateDigitSum(self, n: int) -> int:
        num = str(n)
        res = 0
        for i, d in enumerate(num):
            if i % 2 == 0:
                res += int(d)
            else:
                res -= int(d)
        
        return res
