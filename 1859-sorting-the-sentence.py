class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        res = [""] * len(words)
        for w in words:
            ind = int(w[-1]) - 1
            res[ind] = w[:-1]
        return " ".join(res)
