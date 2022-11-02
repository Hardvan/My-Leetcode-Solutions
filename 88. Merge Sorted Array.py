class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if n==0:
            return
        del nums1[-n:]
        nums1.extend(nums2)
        nums1.sort()
