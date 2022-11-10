class Solution:
    def convertToBase7(self, num: int) -> str:
        temp = num
        if num<0:
            temp*=-1
        
        res = 0
        i = 0
        while(temp>0):
            rem = temp%7
            temp//=7
            res += rem*pow(10,i)
            i += 1
        if num>=0:
            return str(res)
        return "-"+str(res)
