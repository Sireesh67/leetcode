class Solution:
    def check(self, nums: List[int]) -> bool:
        Num = sorted(nums)
        lst = []

        for i in range(len(nums)):
            lst.insert(0, Num.pop())
            if nums == lst + Num:
                return True

        return False