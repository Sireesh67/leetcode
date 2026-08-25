class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)

        def sort_key(x):
            return (freq[x], -x)

        return sorted(nums, key=sort_key)