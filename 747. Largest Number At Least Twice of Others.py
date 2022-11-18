class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        lst = sorted(nums)
        if lst[-1] >= 2*lst[-2]:
            return nums.index(lst[-1])
        else:
            return -1
