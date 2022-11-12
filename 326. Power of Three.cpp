class Solution {
public:
    bool isPowerOfThree(int n) {
        long val = 1;
        if (n<=0) {
            return false;
        }
        while(val<=n) {
            if (val == n) {
                return true;
            }
            val *= 3;
        }
        return false;
    }
};
