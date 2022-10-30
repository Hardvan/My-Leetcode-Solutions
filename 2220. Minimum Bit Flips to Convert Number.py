class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        a = bin(start)[2:]
        b = bin(goal)[2:]
        count = 0
        # Converting a and b to equal length
        a = "0"*abs(len(b)-len(a)) + a
        b = "0"*abs(len(b)-len(a)) + b
        for i in range(len(a)):
            if a[i]!=b[i]:
                count+=1
        return count
