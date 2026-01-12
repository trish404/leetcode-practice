class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        res = 0
        for op in operations:
            if op == "++X" or op == "X++":
                res +=1
            else:
                res -= 1
        return res
