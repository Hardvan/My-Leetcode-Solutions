class Solution {
public:
    void reverseString(vector<char>& s) {
        int n = s.size();
        char temp;
        for(int i=0; i<n/2; i++) {
            int end = n-i-1;
            temp = s[i];
            s[i] = s[end];
            s[end] = temp;
        }
    }
};
