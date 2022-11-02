class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        while True:
            num = ""
            for i in range(n):
                num += str(random.randint(0,1))
            if num not in nums:
                return num
