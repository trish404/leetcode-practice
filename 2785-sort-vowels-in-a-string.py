class Solution:
    def sortVowels(self, s: str) -> str:
        vow = ('aeiouAEIOU')
        ind = []
        v = []
        for i , char in enumerate(s):
            if char in vow:
                ind.append(i)
                v.append(char)
        v.sort()
        ind.sort()
        s = list(s)
        
        for i in range(len(ind)):
            s[ind[i]] = v[i]
        
        return "".join(s)
