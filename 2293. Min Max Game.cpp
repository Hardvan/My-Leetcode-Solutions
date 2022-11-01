class Solution {
public:
    int minMaxGame(vector<int>& nums) {
        while (nums.size()!=1) {
            vector<int> newNums;
            for(int i=0; i<nums.size()/2; i++) {
                int a = nums[2*i];
                int b = nums[2*i+1];
                if(i%2==0) {
                    newNums.push_back(a<b?a:b);
                }
                else {
                    newNums.push_back(a>b?a:b);
                }
            }
            nums = newNums;
        }
        return nums[0];
    }
};
