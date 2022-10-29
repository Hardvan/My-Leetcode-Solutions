class Solution {
public:
    long convert(int no, int base) {
        long ans = 0;
        long power = 1;
        while (no>0) {
            int digit = no%base;
            no/=base;
            ans+=digit*power;
            power*=10;
        }
        return ans;
    }
    bool isPalindrome(int no) {
        int rev=0;
        int temp = no;
        while(temp>0) {
            int digit = temp%10;
            temp/=10;
            rev = rev*10+digit;
        }
        return no==rev;
    }
    bool isPalindrome(long no) {
        long rev=0;
        long temp = no;
        while(temp>0) {
            int digit = temp%10;
            temp/=10;
            rev = rev*10+digit;
        }
        return no==rev;
    }
    bool isStrictlyPalindromic(int n) {
        
        for (int base=2; base<=n-2; base++) {
            if (!isPalindrome(convert(n,base))) {
                return false;
            }
        }
        return true;
    }
};
