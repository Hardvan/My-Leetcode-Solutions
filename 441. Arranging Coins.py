class Solution:
    def arrangeCoins(self, n: int) -> int:
        ans = 0
        coins = n
        for row in range(1,n+1):
            if coins >= row:
                coins -= row
                ans += 1
            else:
                break
        return ans
