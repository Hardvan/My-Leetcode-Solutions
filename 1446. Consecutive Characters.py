class Solution:
    def maxPower(self, s: str) -> int:
        n = len(s)
        count = 1
        maxim = 1
        for i in range(n):
            ch = s[i]
            count = 1
            for j in range(i+1,n):
                if s[j]==ch:
                    count += 1
                    if count > maxim:
                        maxim = count
                else:
                    break
        return maxim
