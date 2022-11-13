class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        a, b = list(bin(x)[2:]), list(bin(y)[2:])
        l1, l2 = len(a), len(b)
        if l1<l2:
            for i in range(l2-l1):
                a.insert(0,"0")
        elif l1>l2:
            for i in range(l1-l2):
                b.insert(0,"0")
        ans = 0
        for i in range(max(len(a),len(b))):
            if a[i]!=b[i]:
                ans += 1
        return ans
