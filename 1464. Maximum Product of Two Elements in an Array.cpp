class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int max = 0;
        int n = nums.size();
        for(int i=0; i<n-1; i++) {
            for(int j=i+1; j<n; j++) {
                int prod = (nums[i]-1)*(nums[j]-1);
                if (prod>max) {
                    max=prod;
                }
            }
        }
        return max;
    }
};
