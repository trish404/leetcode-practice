class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        tot = 0

        for i in range(n):
            tot += mat[i][i]
            tot += mat[i][n-1-i]
        if n % 2 == 1:
            tot -= mat[n//2][n//2]
        return tot
