class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [float('inf')] * (amount + 1) 
        dp[0] = 0
        for coin in coins:
            for curr_amt in range(coin, amount+1):
                dp[curr_amt] = min(dp[curr_amt], dp[curr_amt - coin] + 1)
        
        return dp[amount] if dp[amount]!= float('inf') else -1 



