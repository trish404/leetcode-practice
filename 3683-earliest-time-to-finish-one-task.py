class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        best = 201
        for time in tasks:
            best = min(best, sum(time))

        return best
