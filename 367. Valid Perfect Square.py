class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        val = num**0.5
        return val == int(val)
