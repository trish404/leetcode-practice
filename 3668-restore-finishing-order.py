class Solution(object):
    def recoverOrder(self, order, friends):
        """
        :type order: List[int]
        :type friends: List[int]
        :rtype: List[int]
        """
        res = []
        for x in order:
            if x in friends:
                res.append(x)
        return res
        
