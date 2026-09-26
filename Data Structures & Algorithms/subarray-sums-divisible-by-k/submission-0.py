class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n, res = len(nums), 0
        for i in range(n):
            cSum = 0
            for j in range(i, n):
                cSum += nums[j]
                if cSum % k == 0:
                    res += 1

        return res