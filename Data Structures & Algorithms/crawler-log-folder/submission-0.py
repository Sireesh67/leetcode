class Solution:
    def minOperations(self, logs: List[str]) -> int:
        res = 0
        for i in logs:
            if i == "./":
                continue
            if i == "../":
                res = max(0, res-1)
            else:
                res += 1
        return res