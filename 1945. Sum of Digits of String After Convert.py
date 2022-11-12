class Solution:
    def getLucky(self, s: str, k: int) -> int:
        lst = [str(ord(ch)-ord("a")+1) for ch in s]
        num = int("".join(lst))
        ans = 0
        for i in range(k):
            ans = 0
            # Sum of Digits
            for digit in str(num):
                ans += int(digit)
            num = ans
        return num
