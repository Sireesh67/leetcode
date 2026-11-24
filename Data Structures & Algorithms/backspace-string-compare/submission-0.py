class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def convert(s):
            res = []
            for i in s:
                if char == '#':
                    if res:
                        res.pop()
                else:
                    res.append(i)
            return "".join(res)

        return convert(s) == convert(t)