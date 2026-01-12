class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        best = 0
        for sentence in sentences:
            best = max(best, sentence.count(" ")+1)
        return best
