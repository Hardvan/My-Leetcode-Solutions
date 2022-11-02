class Solution {
public:
    bool checkValid(vector<vector<int>>& mat) {
        int n = mat.size();
        for(int i=0; i<n; i++) {
            vector<int> row, col;
            for(int j=0; j<n; j++) {
                int row_el = mat[i][j];
                int col_el = mat[j][i];
                row.push_back(row_el);
                col.push_back(col_el);
            }
            for(int no=1; no<=n; no++) {
                // Searching
                bool found=false;
                for(int ind=0; ind<n; ind++) { // Row
                    if (no==row[ind]) {
                        found = true;
                        break;
                    }
                }
                if (!found) {
                    return false;
                }
                found=false;
                for(int ind=0; ind<n; ind++) { // Col
                    if (no==col[ind]) {
                        found = true;
                        break;
                    }
                }
                if (!found) {
                    return false;
                }
            }
        }
        return true;
    }
};
