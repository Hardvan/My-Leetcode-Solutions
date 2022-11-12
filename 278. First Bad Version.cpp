// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        int bad;
        int start=1, end=n;
        while (start<=end) {
            bad = start + (end-start)/2;
            if (!isBadVersion(bad)) {
                start = bad + 1;
            }
            else {
                end = bad - 1;
            }
        }
        return start;
    }
};
