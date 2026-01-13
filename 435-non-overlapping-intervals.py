class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[1])  
        res = 0
        end = intervals[0][0]
        for times in intervals: 
            start = times[0]
            if start < end:
                res += 1
            else:
                end = times[1]
        
        return res
