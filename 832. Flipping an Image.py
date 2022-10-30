class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        # ans = []
        # for lst in [i[::-1] for i in image]:
        #     ans.append([1-no for no in lst])
        # return ans
        return [[1-no for no in lst] for lst in [i[::-1] for i in image]]
