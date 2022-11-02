class Solution:
    def freqAlphabets(self, s: str) -> str:
        lst = []
        for i,ch in enumerate(s):
            if ch=="#":
                del lst[-2:]
                lst.append(s[i-2:i])
            else:
                lst.append(ch)
        return "".join([chr(int(i)+96) for i in lst])
