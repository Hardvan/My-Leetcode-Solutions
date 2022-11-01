class Solution {
public:
    double average(vector<int>& salary) {
        int min = salary[0];
        int max = salary[0];
        int sum = 0;
        for(const int &sal:salary) {
            if (sal>max)
                max=sal;
            if (sal<min)
                min=sal;
            sum+=sal;
        }
        return (double(sum-min-max))/(salary.size()-2);
    }
};
