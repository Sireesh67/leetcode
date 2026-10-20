class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        r = 0
        cur = sum(arr[:k-1])
        
        for i in range(len(arr)- k+1):
            cur += arr[i + k-1]
            if (cur/k) >= threshold:
                r += 1
            cur -= arr[i]
        return r

        