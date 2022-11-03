class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        reverse = [int(str(i)[::-1]) for i in nums]
        nums.extend(reverse)
        return len(set(nums))
