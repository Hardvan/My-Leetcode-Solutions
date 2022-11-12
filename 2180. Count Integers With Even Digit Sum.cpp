class Solution {
public:
    int countEven(int num) {
        int count = 0;
        int i;
        int sum, temp, digit;
        for(i=2; i<=num; i++) {
            // Sum of digits
            sum = 0;
            temp = i;
            while(temp>0) {
                digit = temp%10;
                temp/=10;
                sum += digit;
            }
            if (sum%2==0) {
                count++;
            }
        }
        return count;
    }
};
