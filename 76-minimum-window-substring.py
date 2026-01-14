from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = Counter(t)
        miss = len(t)

        l = 0
        best = float('inf')
        best_l = 0

        for r, char in enumerate(s):
            if need[char] > 0:
                miss -= 1
            need[char] -= 1

            while miss == 0:
                wl = r-l+1
                if wl < best:
                    best = wl
                    best_l = l
                
                lch = s[l]
                need[lch] += 1
                if need[lch] > 0:
                    miss += 1

                l += 1
            
        return "" if best == float("inf") else s[best_l:best_l + best]
