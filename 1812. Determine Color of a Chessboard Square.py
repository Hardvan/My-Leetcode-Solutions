class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        a = ord(coordinates[0]) - ord("a") + 1
        b = int(coordinates[1])
        return (a+b)%2!=0
