class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        count = len(words)
        if count %2 == 1:
            return True
        else:
            return False
        