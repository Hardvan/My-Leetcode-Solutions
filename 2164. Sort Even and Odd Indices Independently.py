class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even_ind = sorted(nums[0::2])
        odd_ind = sorted(nums[1::2], reverse = True)
        ans = [0]*len(nums)
        for i in range(len(ans)):
            if i%2==0:
                ans[i] = even_ind.pop(0)
            else:
                ans[i] = odd_ind.pop(0)
        return ans
