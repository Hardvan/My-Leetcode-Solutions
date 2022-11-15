class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int count = 0;
        int maxim = 0;
        int n = nums.size();
        if (n==1) {
            return nums[0]==1;
        }
        for(int i=0; i<n; i++) {
            if (nums[i]!=1) {
                continue;
            }
            else {
                count = 1;
            }
            for(int j=i+1; j<n; j++) {
                // cout << nums[i] << ", " << nums[j] << endl;
                if (nums[j]==1) {
                    count++;
                    if (count > maxim) {
                        maxim = count;
                    }
                    continue;
                }
                else { // 0
                    break;
                }
            }
        }
        return maxim>count?maxim:count;
    }
};
