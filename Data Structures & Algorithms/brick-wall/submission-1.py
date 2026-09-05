class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        cgap = {0: 0}

        for i in wall:
            total = 0
            for j in range(len(i) - 1):
                total += i[j]
                cgap[total] = 1 + cgap.get(total, 0)

        return len(wall) - max(cgap.values())