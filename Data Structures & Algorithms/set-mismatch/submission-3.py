class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        dup = -1
        missing = -1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                dup = nums[i]
            elif nums[i] != nums[i-1] + 1:
                missing = nums[i-1] + 1
        if nums[-1] != len(nums):
            missing = len(nums)
        if nums[0] != 1:
            missing = 1
        return [dup, missing]
        