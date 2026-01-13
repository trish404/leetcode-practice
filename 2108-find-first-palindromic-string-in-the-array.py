class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        word = ""
        for word in words:
            if word == word[::-1]:
                break
            word = ""
        return word
