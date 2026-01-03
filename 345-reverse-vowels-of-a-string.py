class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set('aeiouAEIOU')
        l = []
        
        for char in s:
            if char in vowels:
                l.append(char)
        l.reverse()
        ptr = 0
        s = list(s)
        for i in range(len(s)):
            if s[i] in vowels:
                s[i] = l[ptr]
                ptr += 1

        return "".join(s)


