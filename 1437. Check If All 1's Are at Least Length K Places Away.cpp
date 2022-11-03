class Solution {
public:
    bool kLengthApart(vector<int>& nums, int k) {
        int n = nums.size();
        for(int i=0; i<n; i++) {
            if (nums[i] == 1) {
                int dist = 0;
                for(int j=i+1; j<n; j++) {
                    if (nums[j]==1) {
                        dist = j-i-1;
                        if (dist<k) {
                            return false;
                        }
                        else {
                            break;
                        }
                    }
                    else {
                        continue;
                    }
                }
            }
        }
        return true;
    }
};
