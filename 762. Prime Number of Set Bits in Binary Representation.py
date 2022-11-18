class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        count = 0
        for no in range(left, right+1):
            b = bin(no)[2:]
            n = b.count("1")
            prime = True
            if (n==1):
                continue
            for i in range(2,n//2+1):
                if n==2:
                    break
                if n%i==0:
                    prime = False
                    break
            if prime:
                count += 1
        return count
