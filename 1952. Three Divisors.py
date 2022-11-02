class Solution:
    def isThree(self, n: int) -> bool:
        if n==2:
            return False
        extra = 0
        for i in range(2, n//2+1): #1,n are divisors already
            if n%i==0:
                extra+=1
            if extra > 1:
                return False
        if extra == 0:
            return False
        return True
