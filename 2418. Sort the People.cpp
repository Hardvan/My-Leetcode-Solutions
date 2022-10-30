class Solution {
public:
    vector<string> sortPeople(vector<string>& names, vector<int>& heights) {
        int n = heights.size();
        // Sorting
        for(int i=0; i<n-1; i++) {
            for(int j=i+1; j<n; j++) {
                if (heights[i] < heights[j]) {
                    // Swapping names
                    string temp = names[i];
                    names[i] = names[j];
                    names[j] = temp;
                    int temp2 = heights[i];
                    heights[i] = heights[j];
                    heights[j] = temp2;
                }
            }
        }
        return names;
    }
};
