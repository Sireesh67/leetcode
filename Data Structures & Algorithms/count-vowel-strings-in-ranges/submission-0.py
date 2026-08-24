class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        v = set("aeiou")
        res = []

        for i, j in queries:
            cnt = 0
            for i in range(i, j + 1):
                if words[i][0] in v and words[i][-1] in v:
                    cnt += 1
            res.append(cnt)

        return res