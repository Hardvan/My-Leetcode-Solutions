class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        temp = columnTitle
        i = 0
        while temp != "":
            ch = temp[-1]
            temp = temp[:-1]
            val = ord(ch)-ord("A")+1
            ans += val*pow(26,i)
            i+=1
        return ans
