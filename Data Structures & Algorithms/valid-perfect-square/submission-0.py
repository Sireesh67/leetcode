class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(0 ,num):
            if  i* i > num:
                return False
            if i*i == num:
                return True