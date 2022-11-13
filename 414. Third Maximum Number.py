class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        lst = sorted(list(set(nums)))
        if len(lst) >= 3:
            return lst[-3]
        return lst[-1]
