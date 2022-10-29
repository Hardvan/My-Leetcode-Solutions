class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        vector<int> ans;
        int n=nums.size();
        int i,j;
        for(i=0; i<n; i++) {
            int count = 0;
            for(j=0; j<n; j++) {
                if (nums[j]<nums[i]) {
                    count++;
                }
            }
            ans.push_back(count);
        }
        return ans;
    }
};
