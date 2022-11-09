class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        ans = []
        for arr in nums:
            for i in arr:
                if i in ans:
                    continue
                for j_arr in nums:
                    if i not in j_arr:
                        break
                else:
                    ans.append(i)
        return sorted(ans)
