class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        diff = (nums[-1]-k) - (nums[0]+k)
        if diff < 0:
            return 0
        else:
            return diff
