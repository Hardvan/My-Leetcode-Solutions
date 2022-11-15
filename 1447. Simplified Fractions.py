class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        ans = []
        vals = []
        for numer in range(1,n):
            for denom in range(2,n+1):
                value = numer/denom
                if 0<value<1 and value not in vals:
                    ans.append(f"{numer}/{denom}")
                    vals.append(value)
        return ans
