class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        lst = list(map(int, list(str(n))))
        prod = 1
        for i in lst:
            prod*=i
        return prod-sum(lst)
