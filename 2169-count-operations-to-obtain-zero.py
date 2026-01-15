class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        tot = 0
        while num1 and num2 > 0:
            if num1 < num2:
                num2 -= num1
                tot += 1
            else:
                num1 -= num2
                tot += 1
        return tot
