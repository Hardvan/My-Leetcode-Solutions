class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& nums) {
        vector<int> ans;
        vector<int> odd;
        for(const auto &num : nums) {
            if (num%2==0) {
                ans.push_back(num);
            }
            else {
                odd.push_back(num);
            }
        }
        for(const auto &num : odd) {
            ans.push_back(num);
        }
        return ans;
    }
};
