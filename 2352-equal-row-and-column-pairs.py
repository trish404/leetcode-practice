class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = {}
        for row in grid:
            t = tuple(row)
            if t in rows:
                rows[t] += 1
            else:
                rows[t] = 1
        ans = 0
        for c in range(len(grid)):
            col = tuple(grid[r][c] for r in range(len(grid)))
            if col in rows:
                ans += rows[col]
        
        return ans

        
