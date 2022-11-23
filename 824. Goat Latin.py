class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        ans = []
        words = sentence.split()
        for ind, word in enumerate(words):
            new = ""
            if word[0] in "aeiouAEIOU":
                new = word+"ma"
            else:
                new = word[1:]+word[0]+"ma"
            new += "a"*(ind+1)
            ans.append(new)
        return " ".join(ans)
