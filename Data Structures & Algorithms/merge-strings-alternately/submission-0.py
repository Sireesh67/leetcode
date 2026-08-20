class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a = 0
        b = 0
        st = ""
        while a<len(word1) or b < len(word2):
            if a< len(word1):
                st += word1[a]
                a += 1
            if b < len(word2):
                st += word2[b]
                b += 1
        return st