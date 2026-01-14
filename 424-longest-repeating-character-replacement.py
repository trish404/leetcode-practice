from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        best = 0
        count = {}
        freq = 0
        l = 0
        n = len(s)

        for r in range(n):
            char = s[r]
            count[char] = count.get(char, 0) + 1
            freq = max(freq, count[char])

            while r - l + 1 - freq > k:
                leftchar = s[l]
                count[leftchar] -= 1
                l += 1
            
            best = max(best, r-l+1)
        
        return best
