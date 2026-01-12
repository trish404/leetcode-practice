class Solution(object):
    def merge(self, intervals):
        if not intervals:
            return []
        
        intervals.sort(key= lambda x: x[0])
        res = [intervals[0]]

        for s, e in intervals[1:]:

            last = res[-1][1]
            if s <= last:
                res[-1][1] = max(last, e)
            else:
                res.append([s,e])
        
        return res
