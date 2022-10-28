class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except:
            if target<nums[0]:
                return 0
            for i in range(len(nums)-1):
                a=nums[i]
                b=nums[i+1]
                if a<target<b:
                    return i+1
            else:
                return len(nums)
