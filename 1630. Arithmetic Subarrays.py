class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def checkSequence(lst):
            lst.sort()
            d = lst[1] - lst[0]
            for i in range(len(lst)-1):
                if d!= lst[i+1] - lst[i]:
                    return False
            return True

        ans = []
        for i in range(len(l)):
            ans.append(checkSequence(nums[l[i]:r[i]+1]))
        return ans
