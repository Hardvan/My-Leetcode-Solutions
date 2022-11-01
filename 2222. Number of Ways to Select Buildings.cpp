class Solution {
public:
    long long numberOfWays(string s) {
        int n = s.size();
        int count = 0;
        for(int i=0; i<n-2; i++) {
            for(int j=i+1; j<n-1; j++) {
                for(int k=j+1; k<n; k++) {
                    if (s[i]!=s[j] && s[j]!=s[k]) {
                        count++;
                    }
                }
            }
        }
        return count;
    }
};

// TLE
