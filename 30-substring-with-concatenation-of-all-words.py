from typing import List
from collections import Counter, defaultdict

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        wlen = len(words[0])
        total_words = len(words)
        total_len = wlen * total_words
        if len(s) < total_len:
            return []

        need = Counter(words)
        res = []

        for offset in range(wlen):
            left = offset
            window = defaultdict(int)
            count = 0

            for right in range(offset, len(s) - wlen + 1, wlen):
                w = s[right:right + wlen]

                if w in need:
                    window[w] += 1
                    count += 1

                    while window[w] > need[w]:
                        lw = s[left:left + wlen]
                        window[lw] -= 1
                        left += wlen
                        count -= 1

                    if count == total_words:
                        res.append(left)
                        lw = s[left:left + wlen]
                        window[lw] -= 1
                        left += wlen
                        count -= 1
                else:
                    window.clear()
                    count = 0
                    left = right + wlen

        return res
