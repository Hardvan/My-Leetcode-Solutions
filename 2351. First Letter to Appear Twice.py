class Solution:
    def repeatedCharacter(self, s: str) -> str:
        diction = {}
        for ch in s:
            if ch not in diction:
                diction[ch] = 1
            else:
                diction[ch] += 1
                if diction[ch] == 2:
                    return ch
