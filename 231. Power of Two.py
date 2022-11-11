class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        i = 0
        val = pow(2,i)
        while val<=n:
            if n==val:
                return True
            i += 1
            val = pow(2,i)
        return False
