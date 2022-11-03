class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitudes = [0]
        for h in gain:
            altitudes.append(altitudes[-1] + h)
        return max(altitudes)
