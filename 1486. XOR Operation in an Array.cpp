class Solution {
public:
    int xorOperation(int n, int start) {
        int i;
        // Creating Array
        vector<int> arr;
        int res = start;
        for(i=1; i<n; i++) {
            // arr.push_back(start+2*i);
            res^=(start+2*i);
        }

        // // Bitwise XOR
        // int res = arr[0];
        // for(i=1; i<n; i++) {
        //     res = res ^ arr[i];
        // }

        return res;
    }
};
