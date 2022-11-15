class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        check1 = word.isupper()
        check2 = word.islower()
        check3 = word[0].isupper() and word[1:].islower()
        return check1 or check2 or check3
