class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        sen1 = s1.split()
        sen2 = s2.split()
        all_words = sen1 + sen2
        ans = []
        for word in all_words:
            if (sen1.count(word) == 1 and sen2.count(word) == 0) or (sen2.count(word) == 1 and sen1.count(word) == 0):
                ans.append(word)
        return ans
