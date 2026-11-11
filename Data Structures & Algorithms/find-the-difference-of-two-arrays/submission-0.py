class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        r1, r2 = [], []

        for i in set1:
            if i not in set2:
                r1.append(i)

        for i in set2:
            if i not in set1:
                r2.append(i)

        return [r1, r2]        