class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        vector<bool> result;
        int n = candies.size();
        int i, j;
        for(i=0; i<n; i++) {
            int flag = 1;
            for (j=0; j<n; j++) {
                if (candies[i] + extraCandies < candies[j]) {
                    result.push_back(false);
                    flag = 0;
                    break;
                }
            }
            if (flag)
                result.push_back(true);
        }
        return result;
    }
};
