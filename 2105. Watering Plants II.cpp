class Solution {
public:
    int minimumRefill(vector<int>& plants, int capacityA, int capacityB) {
        int refills = 0;
        int n = plants.size();
        int initialA = capacityA;
        int initialB = capacityB;
        int alice_ind, bob_ind;
        int req_a, req_b;
        for(int i=0; i<n ;i++) {
            alice_ind = i;
            bob_ind = n-i-1;
            req_a = plants[alice_ind];
            req_b = plants[bob_ind];
            if (alice_ind > bob_ind) {
                break;
            }
            else if (alice_ind == bob_ind) {
                // Handle Equality
                if (capacityA > capacityB) {
                    if (capacityA >= req_a) {
                    capacityA -= req_a;
                    }
                    else {
                        capacityA = initialA - req_a;
                        refills+=1;
                    }
                }
                else if (capacityB > capacityA) {
                    if (capacityB >= req_b) {
                        capacityB -= req_b;
                    }
                    else {
                        capacityB = initialB - req_b;
                        refills+=1;
                    }
                }
                else {
                    if (capacityA >= req_a) {
                    capacityA -= req_a;
                    }
                    else {
                        capacityA = initialA - req_a;
                        refills+=1;
                    }
                }
            }
            else if (alice_ind < bob_ind) {
                // Alice Watering
                if (capacityA >= req_a) {
                    capacityA -= req_a;
                }
                else {
                    capacityA = initialA - req_a;
                    refills+=1;
                }

                // Bob Watering
                if (capacityB >= req_b) {
                    capacityB -= req_b;
                }
                else {
                    capacityB = initialB - req_b;
                    refills+=1;
                }
            }
        }
        return refills;
    }
};
