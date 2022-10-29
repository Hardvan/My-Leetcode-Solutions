class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        ans = []
        n = len(grid)
        for i in range(1,n-2+1):
            lst2=[]
            for j in range(1,n-2+1):
                center = grid[i][j]
                lst = []
                for x in [-1,0,1]:
                    for y in [-1,0,1]:
                        lst.append(grid[i+x][j+y])
                lst2.append(max(lst))
            ans.append(lst2)
        return ans
                    
