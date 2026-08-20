class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        i = 0
        j = 1
        arr = []
        while j < len(nums):
            if nums[j]> nums[i]:
                i += 1
                j += 1
            else:
                arr.append(nums[j])
                nums[j]+=1
                arr.append(nums[j])
                i+= 1
                j+= 1
        arr.sort()
        return arr
        