class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        diction = {}
        for i in range(26):
            diction[chr(ord("a")+i)] = ""
        already = []
        i=0
        for ch in key:
            if ch not in already and ch!=" ":
                diction[ch] = chr(ord("a")+i)
                i+=1
                already.append(ch)
        ans = ""
        for ch in message:
            if ch==" ":
                ans+=ch
                continue
            ans+=diction[ch]
        return ans
