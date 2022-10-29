class Solution {
public:
    int maxWidthOfVerticalArea(vector<vector<int>>& points) {
        vector<int> X;
        // vector<int> Y;
        int n=points.size();
        int i,j;
        // // Separating x,y
        // for(i=0; i<n; i++) {
        //     X.push_back(points[i][0]);
        //     // Y.push_back(points[i][1]);
        // }

        // Sorting
        for(i=0; i<n-1; i++) {
            for(j=i+1; j<n; j++) {
                if (points[i][0] > points[j][0]) {
                    int temp = points[i][0];
                    points[i][0] = points[j][0];
                    points[j][0] = temp;
                    // temp = Y[i];
                    // Y[i] = Y[j];
                    // Y[j] = temp;
                }
            }
        }

        // Finding Max Difference between two consecutive elements
        int max=0;
        for(i=0; i<n-1; i++) {
            int diff = points[i+1][0]-points[i][0];
            if (diff > max) {
                max=diff;
            }
        }

        return max;
    }
};

// TLE
