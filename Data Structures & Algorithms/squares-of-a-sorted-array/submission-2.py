class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr = []
        for i in nums:
            arr.append(i*i)
        n = len(arr)
        for i in range(n-1):
            minpos = i
            for j in range (i, n):
                if arr[j]< arr[minpos]:
                    minpos = j

            temp = arr[i]
            arr[i] = arr[minpos]
            arr[minpos] = temp
        return arr