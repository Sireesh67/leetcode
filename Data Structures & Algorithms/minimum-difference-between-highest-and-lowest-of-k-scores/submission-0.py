class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-1] - nums[-2]
        