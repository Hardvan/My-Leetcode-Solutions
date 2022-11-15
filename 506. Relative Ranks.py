class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        lst = sorted(score)[::-1]
        diction = {}
        for ind,i in enumerate(lst):
            text = ""
            if ind == 0:
                text = "Gold Medal"
            elif ind==1:
                text = "Silver Medal"
            elif ind==2:
                text = "Bronze Medal"
            else:
                text = str(ind+1)
            diction[i] = text
        ans = [diction[i] for i in score]
        return ans
