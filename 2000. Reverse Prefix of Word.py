class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        try:
            ind = list(word).index(ch)
        except ValueError:
            return word
        return word[:ind+1][::-1] + word[ind+1:]
