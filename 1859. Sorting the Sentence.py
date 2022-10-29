class Solution:
    def sortSentence(self, s: str) -> str:
        diction = {}
        words = s.split()
        for word in words:
            diction[int(word[-1])] = word[:-1]
        ans = []
        for i in range(1,len(words)+1):
            ans.append(diction[i])
        return " ".join(ans)
