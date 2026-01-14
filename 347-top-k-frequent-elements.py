from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        s = c.most_common()
        res = []
        for i in range(k):
            res.append(s[i][0]) 
        
        return res
