class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower()
        n = len(s)
        a = s[:n//2]
        b = s[n//2:]
        c1 = c2 = 0
        vowels = "a e i o u".split()
        for ch in a:
            if ch in vowels:
                c1 += 1
        for ch in b:
            if ch in vowels:
                c2 += 1
            if c2 > c1: # No need to check further
                return False
        return c1==c2
