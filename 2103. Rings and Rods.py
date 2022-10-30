class Solution:
    def countPoints(self, rings: str) -> int:
        rods = [[] for i in range(10)]
        for i in range(0,len(rings),2):
            color = rings[i]
            rod = int(rings[i+1])
            rods[rod].append(color)
        count=0
        for rod in rods:
            if "R" in rod and "G" in rod and "B" in rod:
                count+=1
        return count
