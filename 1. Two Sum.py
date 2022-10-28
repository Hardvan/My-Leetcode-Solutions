class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a=None
        b=None
        check = False
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    a=i
                    b=j
                    check = True
                    break
            if check:
                break
        
        return a,b
