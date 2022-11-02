class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                top = left = right = bottom = -1
                val = mat[i][j]
                try:
                    top = mat[i-1][j]
                except:
                    pass
                try:
                    bottom = mat[i+1][j]
                except:
                    pass
                try:
                    right = mat[i][j+1]
                except:
                    pass
                try:
                    left = mat[i][j-1]
                except:
                    pass
                if val > max(top,bottom,left,right):
                    return [i,j]
