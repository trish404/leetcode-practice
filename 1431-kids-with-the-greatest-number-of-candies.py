class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        res = []
        for i in range(len(candies)):
            tot = candies[i] + extraCandies
            newList = candies[:]
            newList.pop(i)
            mx = max(newList) if newList else 0
            res.append(tot >= mx)
        return res
