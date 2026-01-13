class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        avg = []
        for i in range(len(nums)//2):
            small = min(nums)
            big = max(nums)
            nums.remove(small)
            nums.remove(big)
            avg.append((small+big)/2)
        
        return min(avg)
