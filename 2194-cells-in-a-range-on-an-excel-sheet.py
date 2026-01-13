class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        c1, r1, _, c2, r2 = s[0], s[1], s[2], s[3], s[4]
        res = []
        for c in range(ord(c1), ord(c2)+1):
            for r in range(int(r1), int(r2)+1):
                res.append(chr(c)+str(r))
        return res
