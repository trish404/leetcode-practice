class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        d = 0
        u = 0 
        while mainTank > 0:
            mainTank -= 1
            d += 10
            u += 1

            if u % 5 == 0 and additionalTank > 0:
                mainTank += 1
                additionalTank -= 1

        return d
