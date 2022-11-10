class Solution {
public:
    int findNumbers(vector<int>& nums) {
        int count = 0;
        int c;
        for(auto n : nums) {
            c = 0;
            while(n>0) {
                c++;
                n/=10;
            }
            if (c%2==0) {
                count++;
            }
        }
        return count;
    }
};
