class Solution {
public:
    bool checkIfPangram(string sentence) {
        for(int i=0; i<26; i++) {
            int flag=0;
            for(auto &ch_str : sentence) {
                if (char(97+i)==ch_str) {
                    flag=1;
                    break;
                }
            }
            if (!flag)
                return false;
        }
        return true;
    }
};
