class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if nums.count(0)==0:
            return len(nums) - 1
        maxi = 0
        for ind, digit in enumerate(nums):
            if digit==0:
                # Finding the longest length of 1's
                for seq in "".join(map(str, nums[:ind] + nums[ind+1:])).split("0"):
                    if len(seq) > maxi:
                        maxi=len(seq)
        return maxi
