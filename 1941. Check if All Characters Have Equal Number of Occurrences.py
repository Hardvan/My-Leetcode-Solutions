class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        unique = list(set(s))
        count = s.count(unique[0])
        for ch in unique:
            if s.count(ch) != count:
                return False
        return True
