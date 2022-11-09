class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        dis = 1
        for s in arr:
            if arr.count(s) == 1:
                if dis == k:
                    return s
                dis += 1
        return ""
