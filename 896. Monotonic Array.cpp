class Solution {
public:
    bool isMonotonic(vector<int>& nums) {
        int asc = 0;
        int des = 0;
        for(auto i=0; i<nums.size()-1; i++) {
            if (nums[i+1] > nums[i]) {
                asc += 1;
            }
            else if (nums[i+1] < nums[i]) {
                des += 1;
            }
            else {
                continue;
            }
            if (asc*des!=0) { // Only ascending or descending
                return false;
            }
        }
        return true;
    }
};
