class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine = list(magazine)
        for ch in ransomNote:
            if ch not in magazine:
                return False
            else:
                magazine.remove(ch)
        return True
