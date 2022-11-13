class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        t = list(t)
        for ch in s:
            t.remove(ch)
        return t[0]
