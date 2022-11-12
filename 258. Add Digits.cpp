class Solution {
public:
    int addDigits(int num) {
        int sum;
        int digit;
        while (true) {
            sum = 0;
            while (num>0) {
                digit = num%10;
                num/=10;
                sum += digit;
            }
            if (sum<10) {
                return sum;
            }
            else {
                num = sum;
            }
        }
        return sum;
    }
};
