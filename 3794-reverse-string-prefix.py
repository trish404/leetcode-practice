class Solution(object):
    def reversePrefix(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s1 = s[:k]
        s2 = s[k:]

        s1 = s1[::-1]

        return s1 + s2
