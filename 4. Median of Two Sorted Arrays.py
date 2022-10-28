class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        lst = sorted(nums1)
        l = len(lst)
        median = None
        if l%2!=0:
            median = lst[(l+1)//2-1]
        else:
            median = (lst[l//2-1] + lst[l//2])/2
        return median
