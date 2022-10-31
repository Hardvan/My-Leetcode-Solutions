class Solution {
public:
    vector<vector<int>> matrixBlockSum(vector<vector<int>>& mat, int k) {
        vector<vector<int>> ans;
        int m = mat.size();
        int n = mat[0].size();
        for (int i=0; i<m; i++) {
            vector<int> temp;
            for(int j=0; j<n; j++) {
                int sum = 0;
                for(int r=i-k; r<=i+k; r++) {
                    if (r<0 || r>=m)
                        continue;
                    for(int c=j-k; c<=j+k; c++) {
                        if (c<0 || c>=n)
                            continue;
                        sum+=mat[r][c];
                    }
                }
                temp.push_back(sum);
            }
            ans.push_back(temp);
        }
        return ans;
    }
};
