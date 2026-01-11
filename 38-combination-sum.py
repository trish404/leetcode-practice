class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()

        def backtrack(start, curr, target):
            if target == 0:
                res.append(curr)
                return
            
            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    break
                backtrack(i, curr + [candidates[i]], target - candidates[i])
            
            return 
            
        backtrack(0, [], target)
        return res
            
