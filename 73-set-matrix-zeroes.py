class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c = len(matrix[0])
        i = 0
        res = []

        for row in range(r):
            for col in range(c):
                if matrix[row][col] == 0:
                    res.append([row,col])

        
        cols = []
        rows = []
        for entry in res:
            rows.append(entry[0])
            cols.append(entry[1])
        
        rows = set(rows)
        cols = set(cols)

        for i in range(r):
            for j in range(c):
                if i in rows or j in cols:
                    matrix[i][j] = 0
                    
        return matrix
