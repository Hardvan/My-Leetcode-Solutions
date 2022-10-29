class Solution {
public:
    vector<int> countPoints(vector<vector<int>>& points, vector<vector<int>>& queries) {
        vector<int> ans;
        int i,j;
        for(j=0; j<queries.size(); j++) { // Each Circle
            int count=0;
            for(i=0; i<points.size(); i++) { // Each Point
                if ((points[i][0]-queries[j][0])*(points[i][0]-queries[j][0]) + (points[i][1]-queries[j][1])*(points[i][1]-queries[j][1]) - queries[j][2]*queries[j][2]<=0) {
                    count++;
                }
            }
            ans.push_back(count);
        }
        return ans;
    }
};
