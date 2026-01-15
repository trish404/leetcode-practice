class Solution:
    def countDigits(self, num: int) -> int:
        tot = 0
        for ch in str(num):
            d = int(ch)
            if d != 0 and num % d == 0:
                tot += 1
        return tot
