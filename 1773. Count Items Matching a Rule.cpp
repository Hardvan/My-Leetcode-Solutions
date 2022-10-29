class Solution {
public:
    int countMatches(vector<vector<string>>& items, string ruleKey, string ruleValue) {
        int count = 0;
        for(int i=0; i<items.size(); i++) {
            if ((ruleKey == "type" and ruleValue == items[i][0]) || (ruleKey == "color" and ruleValue == items[i][1]) || (ruleKey == "name" and ruleValue == items[i][2])) {
                count++;
            }
        }
        return count;
        
    }
};
