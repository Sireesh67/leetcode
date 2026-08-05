class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        substrings = [w1 for w1 in words if any(w1 in w2 for w2 in words if w1 != w2)]
        return substrings