class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        n1 = num1.split("+")
        n2 = num2.split("+")
        return f'{int(n1[0]) * int(n2[0]) - int(n1[1][:-1]) * int(n2[1][:-1])}+{int(n1[0]) * int(n2[1][:-1]) + int(n2[0]) * int(n1[1][:-1])}i'
