class Solution {
public:
    string replaceDigits(string s) {
        for(int i=1; i<s.size(); i+=2) {
            s[i] = char(int(s[i-1]) + int(s[i]) - 48); // int('0') = 48
        }
        return s;
    }
};
