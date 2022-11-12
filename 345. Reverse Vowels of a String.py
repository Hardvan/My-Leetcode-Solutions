class Solution:
    def reverseVowels(self, s: str) -> str:
        a = list(s)
        vowels = []
        for ind,ch in enumerate(a):
            if ch.lower() in "aeiou":
                a[ind] = "_"
                vowels.append(ch)
        print(a,vowels)
        for ind, ch in enumerate(a):
            if ch == "_":
                a[ind] = vowels[-1]
                vowels.pop()
        return "".join(a)
