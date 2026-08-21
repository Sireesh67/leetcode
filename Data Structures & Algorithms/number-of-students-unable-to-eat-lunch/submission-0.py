class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        r = len(students)
        cnt = Counter(students)

        for c in sandwiches :
            if cnt[c] > 0:
                r -= 1
                cnt[c] -= 1
            else:
                return r
        return r