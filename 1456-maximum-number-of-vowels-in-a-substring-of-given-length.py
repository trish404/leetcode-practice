class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        mx = 0
        vowels = set("aeiouAEIOU")
        curr = 0
        for i in range(k):
            if s[i] in vowels:
                curr += 1
        
        mx = curr

        for i in range(k, len(s)):
            if s[i] in vowels:
                curr += 1
            if s[i-k] in vowels:
                curr -= 1
            if curr > mx:
                mx = curr

        return mx
