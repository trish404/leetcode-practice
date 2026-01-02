class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        total = len(word1) + len(word2)
        for x in range(0, total):
            if len(word1) > 0:
                merged = merged + word1[:1]
                word1 = word1[1:]
            if len(word2) > 0:
                merged = merged + word2[:1]
                word2 = word2[1:]
        return merged
            
        
