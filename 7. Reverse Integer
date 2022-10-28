class Solution:
    def reverse(self, x: int) -> int:
        if x>=0:
            value = int(str(x)[::-1])
            if value <-2**31 or value > 2**31-1:
                return 0
            return value
        else:
            value = -int(str(abs(x))[::-1])
            if value < (-2**31) or value > (2**31-1):
                return 0
            return value
