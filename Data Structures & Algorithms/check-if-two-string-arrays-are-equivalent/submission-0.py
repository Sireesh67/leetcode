class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        s1 = "".join(word1)
        i = 0
        for w in word2:
            for c in w:
                if i == len(s1) or s1[i] != c:
                    return False
                i += 1
        return i == len(s1)