class Solution {
public:
    int minOperations(vector<int>& nums) {
        int ops = 0;
        int n = nums.size();
        for(int i=0; i<n-1; i++) {
            if (nums[i+1] > nums[i]) { // Increasing
                continue;
            }
            else {
                ops = ops + nums[i] - nums[i+1] + 1;
                nums[i+1] = nums[i]+1;
            }
            
            // while(!(nums[i+1]>nums[i])) {
            //     nums[i+1]++;
            //     ops++;
            // }
        }
        return ops;
    }
};
