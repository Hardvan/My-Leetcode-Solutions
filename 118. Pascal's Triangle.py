class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def fact(n):
            if n<=1:
                return 1
            return n*fact(n-1)
    
        def ncr(n,r):
            return int(fact(n)/(fact(r)*fact(n-r)))

        ans = []
        for i in range(numRows):
            lst = []
            for j in range(i+1):
                lst.append(ncr(i,j))
            ans.append(lst)
        return ans
