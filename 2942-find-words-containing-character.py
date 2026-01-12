class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        res = []
        n = len(words)
        for i, w in enumerate(words):
            if x in w:
                res.append(i)
        return res
