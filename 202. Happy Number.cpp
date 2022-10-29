class Solution {
public:
    int getExp(int no) {
        int sum = 0;
        while(no>0) {
            sum += (no%10)*(no%10);
            no/=10;
        }
        return sum;
    }
    bool isHappy(int n) {
        
        int exp = getExp(n);
        int i=0;
        while (1) {
            if (exp == 1) {
                return true;
            }
            exp = getExp(exp);
            i++;
            if (i>=100) {
                break;
            }
        }
        return false;
    }
};
