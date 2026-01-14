from math import gcd
class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        res = []
        for denom in range(2, n+1):
            for num in range(1, denom):
                if gcd(num, denom) == 1:
                    res.append(f"{num}/{denom}")
        
        return res
