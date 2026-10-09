class Solution:
    def arrangeCoins(self, n: int) -> int:
        r = 0
        while n - r > 0:
            r += 1
            n -= r
        return r
        