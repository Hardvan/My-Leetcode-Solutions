class Solution:
    def sumBase(self, n: int, k: int) -> int:
        # Conversion
        res = 0
        i = 0
        while(n>0):
            rem = n%k
            n//=k
            res += rem*pow(10,i)
            i+=1
        # Summation
        s = 0
        for digit in str(res):
            s += int(digit)
        return s
