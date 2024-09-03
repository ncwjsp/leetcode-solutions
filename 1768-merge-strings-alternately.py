class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        newStr = ""
        while word1 or word2:
            newStr += word1[:1]
            word1 = word1[1:]
            newStr += word2[:1]
            word2 = word2[1:]
        return newStr