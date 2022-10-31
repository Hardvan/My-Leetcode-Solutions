class Solution {
public:
    int maxSum(vector<vector<int>>& grid) {
        int n = grid.size();
        int m = grid[0].size();
        int max=0;
        for(int ci=1; ci<n-1; ci++) {
            for(int cj=1; cj<m-1; cj++) {
                int sum = grid[ci-1][cj-1] + grid[ci-1][cj] + grid[ci-1][cj+1] + grid[ci][cj] + grid[ci+1][cj-1] + grid[ci+1][cj] + grid[ci+1][cj+1];
                if (sum>max)
                    max=sum;
            }
        }
        return max;
    }
};
