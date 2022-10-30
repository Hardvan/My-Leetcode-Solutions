class Solution {
public:
    int countGoodTriplets(vector<int>& arr, int a, int b, int c) {
        int count=0;
        int n=arr.size();
        for(int i=0; i<n-2; i++) {
            for(int j=i+1; j<n-1; j++) {
                for(int k=j+1; k<n; k++) {
                    int diff1 = arr[i] - arr[j];
                    if (diff1<0) diff1*=-1;
                    int diff2 = arr[j] - arr[k];
                    if (diff2<0) diff2*=-1;
                    int diff3 = arr[i] - arr[k];
                    if (diff3<0) diff3*=-1;

                    if (diff1<=a && diff2<=b && diff3<=c) {
                        count+=1;
                    }
                }
            }
        }
        return count;
    }
};
