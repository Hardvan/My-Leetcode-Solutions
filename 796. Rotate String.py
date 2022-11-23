class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)):
            new_s = s[1:] + s[0]
            if new_s==goal:
                return True
            s = new_s
        return False
