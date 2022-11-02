class Solution {
public:
    bool checkXMatrix(vector<vector<int>>& grid) {
        int n = grid.size();
        for(int i=0; i<n; i++) {
            if(grid[i][i] == 0 || grid[i][n-i-1] == 0) { // Diagonal Elements Non-Zero
                return false;
            }
            for(int j=0; j<n; j++) {
                if (j==i || j==n-i-1) {
                    continue;
                }
                if (grid[i][j]!=0 || grid[j][i] != 0) { // Other elements zero
                    return false;
                }
            }
        }
        return true;
    }
};
