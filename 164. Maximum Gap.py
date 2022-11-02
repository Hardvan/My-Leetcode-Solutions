class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n<2:
            return 0
        nums = sorted(nums)
        max_diff = 0
        for i in range(n-1):
            diff = nums[i+1] - nums[i]
            if diff > max_diff:
                max_diff = diff
        return max_diff
