class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        diction = {}
        for val, w in sorted(items1 + items2):
            if val in diction:
                diction[val] += w
            else:
                diction[val] = w
        ans = [[val, diction[val]] for val in diction]
        return ans
