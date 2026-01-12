class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        """
        :type hours: List[int]
        :type target: int
        :rtype: int
        """
        tot = 0
        for i in hours:
            if i >= target:
                tot += 1
        
        return tot
        
