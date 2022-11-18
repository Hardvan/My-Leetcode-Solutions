class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums = sorted(nums)
        for num in nums:
            if num==original:
                original*=2
        return original
