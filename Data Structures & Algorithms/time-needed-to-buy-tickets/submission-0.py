class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        r = 0

        for i in range(len(tickets)):
            if i <= k:
                r += min(tickets[i], tickets[k])
            else:
                r += min(tickets[i], tickets[k] - 1)

        return r