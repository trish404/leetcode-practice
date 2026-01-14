class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()

        m = float('inf')
        res = []
        n = len(arr)
        for i in range(n-1):
            d = abs(arr[i+1] - arr[i])
            if d<m:
                m = d
                res = [[arr[i], arr[i+1]]]
            elif m == d:
                res.append([arr[i], arr[i+1]])
        
        return res

