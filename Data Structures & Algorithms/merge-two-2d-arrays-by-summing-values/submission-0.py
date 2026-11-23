class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        t = [0] * 1001
        for i in (nums1, nums2):
            for key, value in i:
                t[key] += value
        return [[key, value] for key, value in enumerate(t) if value]
