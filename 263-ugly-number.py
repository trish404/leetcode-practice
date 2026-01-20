class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        for prim in [2, 3, 5]:
            while n % prim == 0:
                n //= prim

        return n == 1
