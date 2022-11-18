class Solution:
    def largestInteger(self, num: int) -> int:
        ans = num # Initial Value
        s = list(str(num))
        n = len(s)
        for i in range(n):
            for j in range(i+1, n):
                a, b = int(s[i]), int(s[j])
                if (a%2==0 and b%2==0) or (a%2!=0 and b%2!=0):
                    swap = list(s)
                    swap[i], swap[j] = swap[j], swap[i]
                    swap = int("".join(swap))
                    if swap > ans:
                        ans = swap
                        s = list(str(swap))
        return ans
