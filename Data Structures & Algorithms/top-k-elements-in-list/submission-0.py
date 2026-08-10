class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}
        count = 1
        lst = []

        for i in nums:
            dict1[i] = dict1.get(i , 0)+1
        while count <= k:
            maximum = max(dict1 , key = dict1.get)
            del dict1[maximum]
            lst.append(maximum)
            count += 1
        return lst
