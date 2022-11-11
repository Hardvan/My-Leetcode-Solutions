class Solution {
public:
    int bits(int no) {
        int count = 0;
        while(no>0) {
            if (no%2==1) {
                count++;
            }
            no/=2;
        }
        return count;
    }
    vector<int> countBits(int n) {
        

        vector<int> ans;
        for(int i=0; i<n+1; i++) {
            ans.push_back(bits(i));
        }
        return ans;
    }
};
