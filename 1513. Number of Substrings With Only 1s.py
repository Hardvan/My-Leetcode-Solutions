class Solution:
    def numSub(self, s: str) -> int:
        ans = 0
        n = len(s)
        if s.count("1") == n:
            return n*(n+1)//2
        for l in range(1, n):
            for start in range(n):
                end = start+l
                if 0<=start<n and start<end<=n:
                    pass
                else:
                    continue
                sub = s[start:end]
                # print(sub)
                if sub.count("0") == 0 and sub.count("1")>=1:
                    ans+=1
        return ans

# TLE
