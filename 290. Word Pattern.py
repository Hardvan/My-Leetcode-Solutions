class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        diction = {}
        words = s.split()
        if len(pattern) != len(words):
            return False
        for ch,word in zip(pattern, words):
            if ch not in diction:
                diction[ch] = word # a: dog
                # Same mapping (a: dog, b:dog)
                if list(diction.values()).count(word) > 1:
                    return False
            else:
                if diction[ch] != word: # Not Matching
                    return False
        return True
