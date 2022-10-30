class Solution:
    def countAsterisks(self, s: str) -> int:
        words = s.split("|")
        count = 0
        for i in range(0,len(words),2):
            count += words[i].count("*")
        return count
