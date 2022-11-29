class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even_ind = sorted(nums[0::2])
        odd_ind = sorted(nums[1::2], reverse = True)
        ans = []
        for i in range(len(nums)):
            if i%2==0:
                ans.append(even_ind.pop(0))
            else:
                ans.append(odd_ind.pop(0))
        return ans
