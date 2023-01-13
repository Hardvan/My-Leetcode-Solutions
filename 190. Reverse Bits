class Solution:
    def reverseBits(self, n: int) -> int:
        # print(bin(n)[2:])
        lst = list(bin(n)[2:])
        for i in range(32-len(lst)):
            lst.insert(0, "0")
        
        a = "".join(lst)
        # print(a)
        b = a[::-1]
        return int(b, 2)
