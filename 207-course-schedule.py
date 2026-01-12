from collections import deque

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        premap = {i:[] for i in range(numCourses)}

        for c, p in prerequisites:
            premap[c].append(p)
        
        visit = set()

        def dfs(crs):
            if crs in visit:
                return False
            if premap[crs] == []:
                return True
            
            visit.add(crs)
            for pre in premap[crs]:
                if not dfs(pre): return False
            visit.remove(crs)
            premap[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True
