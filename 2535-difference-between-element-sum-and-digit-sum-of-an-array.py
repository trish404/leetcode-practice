class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def ele(num):
            res = 0
            if num < 10:
                return num
            while num > 0:
                res += num%10
                num = num // 10
            
            return res
        
        el = sum(nums)
        dig = 0
        for x in nums:
            dig += ele(x)
        
        return abs(el-dig)


        
