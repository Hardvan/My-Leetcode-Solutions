class Solution:
    def maximum69Number (self, num: int) -> int:
        maxi = num
        num = list(str(num))
        for i in range(len(num)):
            a = list(num)
            if a[i]=="6":
                a[i]="9"
            else:
                a[i]="6"
            a = int("".join(a))
            if a>maxi:
                maxi=a
        return maxi
