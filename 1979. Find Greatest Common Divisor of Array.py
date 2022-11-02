class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums = sorted(nums)
        a = nums[0]
        b = nums[-1]
        gcd = 1
        for i in range(2,a+1):
            if a%i==0 and b%i==0:
                gcd = i
        return gcd
