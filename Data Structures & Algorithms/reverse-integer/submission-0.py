class Solution:
    def reverse(self, x: int) -> int:
        org_num = x
        pos_num = abs(x)

        rev_num = int(str(pos_num)[::-1])

        if org_num < 0:
            rev_num *= -1

        if rev_num < -(1 << 31) or rev_num > (1 << 31) - 1:
            return 0

        return rev_num