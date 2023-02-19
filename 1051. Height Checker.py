class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = 0
        h2 = sorted(heights)
        print(heights)
        for i in range(len(heights)):
            if heights[i] != h2[i]:
                count += 1
        
        return count
