from collections import Counter

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = Counter(arr)
        res = -1

        for num, freq in count.items():
            if num == freq:
                res = max(res, num)

        return res