class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        count = 0
        for sub in patterns:
            if sub in word:
                count+=1
        return count
