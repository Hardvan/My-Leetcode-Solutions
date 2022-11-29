class Solution:
    def binaryGap(self, n: int) -> int:
        b = bin(n)[2:]
        length = len(b)
        maxim = 0
        for i in range(length):
            if b[i] == "1":
                pass
            else:
                continue
            for j in range(i+1,length):
                if b[j] == "1":
                    dist = j-i
                    if dist > maxim:
                        maxim = dist
                    break
                else:
                    continue
        
        return maxim
