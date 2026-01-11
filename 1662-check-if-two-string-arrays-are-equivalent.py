class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        one = ""
        for s in word1:
            one += s

        two = ""
        for s in word2:
            two += s

        return one == two 
        
