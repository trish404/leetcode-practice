class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()

        def backtrack(start, curr, tot):
            if tot == target:
                res.append(list(curr))
                return
            if tot > target:
                return
            
            for i in range(start, len(candidates)):
                num = candidates[i]
                curr.append(num)
                backtrack(i, curr, tot + num)
                curr.pop()
        backtrack(0, [], 0)
        return res
            
