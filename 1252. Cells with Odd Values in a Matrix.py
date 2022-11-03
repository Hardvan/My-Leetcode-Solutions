class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        mat = [[0 for j in range(n)] for i in range(m)]
        print(mat)
        odd_values = 0
        for ri,ci in indices:
            # Incrementing ri
            for col in range(n):
                mat[ri][col] += 1
                if (mat[ri][col]%2!=0):
                    odd_values+=1
                else:
                    odd_values-=1
            # Incrementing ci
            for row in range(m):
                mat[row][ci] += 1
                if (mat[row][ci]%2!=0):
                    odd_values+=1
                else:
                    odd_values-=1
        
        return odd_values
