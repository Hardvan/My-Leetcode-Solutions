class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for i in range(26):
            ch = chr(ord("a")+i)
            if s.count(ch) != t.count(ch):
                return False
        return True
