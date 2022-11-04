class Solution:
    def customSortString(self, order: str, s: str) -> str:
        lst = list(s)
        ans = ""
        for ch in order:
            while lst.count(ch)>0:
                ans += ch
                lst.remove(ch)
        ans += "".join(lst)
        return ans
