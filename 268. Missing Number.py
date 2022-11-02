class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return round((n)*(n+1)/2 - sum(nums))
