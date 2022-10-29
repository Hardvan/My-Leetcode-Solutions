class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        for el in candies:
            for i in candies:
                if el+extraCandies<i:
                    result.append(False)
                    break
            else:
                result.append(True)
        return result
