class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        n = len(word)
        i = word.find(ch)
        r = word[:i+1]
        l = word[i+1:]
        r = r[::-1]
        return r+l
