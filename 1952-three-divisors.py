class Solution:
    def isThree(self, n: int) -> bool:
        res = []
        for i in range(1, (n//2)+1):
            if n % i == 0:
                res.append(i)
        
        return (len(res)+1) == 3
