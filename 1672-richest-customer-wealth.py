class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        res = 0
        for acc in accounts:
            res = max(res, sum(acc))
        return res
        
