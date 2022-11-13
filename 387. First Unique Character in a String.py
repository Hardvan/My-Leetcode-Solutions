class Solution:
    def firstUniqChar(self, s: str) -> int:
        for ind,ch in enumerate(s):
            if s.count(ch) == 1:
                return ind
        return -1
