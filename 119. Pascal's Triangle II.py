class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def fact(n):
            if n<=1:
                return 1
            return n*fact(n-1)
        def ncr(n,r):
            return int(fact(n)/(fact(r)*fact(n-r)))
        return [ncr(rowIndex,j) for j in range(rowIndex+1)]
