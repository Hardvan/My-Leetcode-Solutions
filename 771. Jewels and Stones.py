class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for ch in jewels:
            count += stones.count(ch)
        return count
