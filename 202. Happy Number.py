class Solution:
    def isHappy(self, n: int) -> bool:
        exp = sum(map(lambda x:x*x, map(int, list(str(n)))))
        if exp == 1:
            return True
        i=0
        while True:
            exp = sum(map(lambda x:x*x, map(int, list(str(exp)))))
            if exp==1:
                return True
            i+=1
            if i>=100:
                break
            continue
        return False
