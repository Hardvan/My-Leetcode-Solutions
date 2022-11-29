class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        for a in range(n-3):
            for b in range(a+1,n-2):
                for c in range(b+1,n-1):
                    for d in range(c+1,n):
                        if a==b or b==c or c==d or d==a or (not a<b<c<d):
                            continue
                        if nums[a] + nums[b] + nums[c] == nums[d]:
                            count += 1
        
        return count
