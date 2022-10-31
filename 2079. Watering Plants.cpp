class Solution {
public:
    int wateringPlants(vector<int>& plants, int capacity) {
        int ans=0;
        int initial = capacity;
        for (int i=0; i<plants.size(); i++) {
            int req = plants[i];
            if (capacity>=req) { // Sufficient water
                capacity-=req;
                ans+=1;
            }
            else { // Not sufficient water
                capacity = initial - req;
                ans+=2*i+1;
            }
        }
        return ans;
    }
};
