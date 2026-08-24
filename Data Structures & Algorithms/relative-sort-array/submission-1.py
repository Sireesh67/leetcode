class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        end = []
        set1 = defaultdict(int)
        set2 = set(arr2)

        for i in arr1:
            if i not in arr2:
                end.append(i)
            set1[i] += 1
        
        for n in arr2:
            for j in range(set1[n]):
                res.append(n)
        end.sort()
        return res + end
