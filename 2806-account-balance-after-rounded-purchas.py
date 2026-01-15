class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        r = purchaseAmount % 10
        res = purchaseAmount - r if r < 5 else purchaseAmount + (10 - r)
        return 100 - res
