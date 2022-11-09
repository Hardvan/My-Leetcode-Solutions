class Solution {
public:
    vector<int> selfDividingNumbers(int left, int right) {
        vector<int> ans;
        int temp;
        int digit;
        for(int no=left; no<=right; no++) { // Each Number
            temp = no;
            bool check = true;
            while(temp>0) { // Each digit
                digit = temp%10;
                temp/=10;
                if (digit==0 || no%digit!=0) {
                    check = false;
                    break;
                }
            }
            if (check) {
                ans.push_back(no);
            }
        }
        return ans;
    }
};
