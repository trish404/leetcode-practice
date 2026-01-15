class Solution(object):
    def longestPalindrome(self, s):
        if not s or len(s) < 1:
            return ""
        
        st = 0
        e = 0

        def expandfrommid(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1
        
        for i in range(len(s)):
            l1 = expandfrommid(s, i, i)
            l2 = expandfrommid(s, i, i+1)
            max_l = max(l1, l2)

            if max_l > e - st:
                st = i - (max_l-1) // 2
                e = i + max_l // 2
        
        return s[st:e+1]


        
