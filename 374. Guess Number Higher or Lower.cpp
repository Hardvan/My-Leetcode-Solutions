/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */

class Solution {
public:
    int guessNumber(int n) {
        int start = 1, end = n;
        int middle;
        short val;
        while (start<=end) {
            middle = start + (end-start)/2;
            val = guess(middle); // API Call
            if (val == 0) { // No. Found
                return middle;
            }
            else if (val == 1) {
                start = middle + 1;
            }
            else {
                end = middle - 1;
            }
        }
        return middle;

        // TLE
        // long num = n/2;
        // short val;
        // while (true) {
        //     val = guess(num);
        //     if (val==0) {
        //         return num;
        //     }
        //     num += val;
        // }
        // return num;
    }
};
