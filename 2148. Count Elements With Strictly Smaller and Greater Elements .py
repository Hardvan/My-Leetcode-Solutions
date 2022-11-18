class Solution:
    def countElements(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        nums = sorted(nums)
        n -= nums.count(nums[0])-1 # Removing Repeated Min number
        n -= nums.count(nums[-1])-1  # Removing Repeated Max number
        if n>2:
            return n-2
        else:
            return 0
