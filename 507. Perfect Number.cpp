class Solution {
public:
    bool checkPerfectNumber(int num) {
        if (num%2!=0) {
            return false;
        }
        int sum = 0;
        for(int i=1; i<num; i++) {
            sum += num%i==0?i:0;
        }
        return sum == num;
    }
};
