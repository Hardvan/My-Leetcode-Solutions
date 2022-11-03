class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        lst = [min(a,b) for a,b in rectangles]
        return lst.count(max(lst))
