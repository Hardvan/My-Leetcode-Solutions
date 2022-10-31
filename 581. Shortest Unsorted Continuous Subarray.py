class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        nums_sort = sorted(nums)
        n = len(nums)
        start = 0
        end = -1
        for i in range(n):
            if nums[i] != nums_sort[i]:
                start = i
                break
        for i in range(n):
            if nums[n-i-1] != nums_sort[n-i-1]:
                end = n-i-1
                break
        return end-start+1
