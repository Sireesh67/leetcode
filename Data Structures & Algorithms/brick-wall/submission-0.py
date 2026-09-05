class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        countGap = {0: 0}

        for i in wall:
            total = 0
            for j in range(len(i) - 1):
                total += i[j]
                countGap[total] = 1 + countGap.get(total, 0)

        return len(wall) - max(countGap.values())