class Solution(object):
    def addedInteger(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        x = sum(nums1) 
        y = sum(nums2)
        r = y - x
        return r / len(nums1)
