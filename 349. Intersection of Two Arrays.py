class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # ans = []
        # for i in nums1:
        #     if i in nums2 and i not in ans:
        #         ans.append(i)
        # return ans
        ans = [i for i in nums1 if i in nums2]
        return list(set(ans))
