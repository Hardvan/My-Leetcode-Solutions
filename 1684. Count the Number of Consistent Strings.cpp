class Solution {
public:
    int countConsistentStrings(string allowed, vector<string>& words) {
        int count=0;
        for(int i=0; i<words.size(); i++) { // Each Word
            bool flag=true;
            for(int j=0; j<words[i].size(); j++) { // Each character
                bool found=false;
                for(int k=0; k<allowed.size(); k++) { // Searching for character in allowed
                    if (words[i][j] == allowed[k]) {
                        found = true;
                        break;
                    }
                }
                if(!found) {
                    flag=false;
                    break;
                }
            }
            if (flag) {
                count++;
            }
        }
        return count;
    }
};
