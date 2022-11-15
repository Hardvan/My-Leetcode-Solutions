class Solution:
    def findComplement(self, num: int) -> int:
        rev = bin(num)[2:]
        ans = ""
        for bit in rev:
            ans += str(ord("1") - ord(bit)) # Complementing
        return int(ans,2)
