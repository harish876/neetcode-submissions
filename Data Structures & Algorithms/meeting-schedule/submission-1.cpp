/**
 * Definition of Interval:
 * class Interval {
 * public:
 *     int start, end;
 *     Interval(int start, int end) {
 *         this->start = start;
 *         this->end = end;
 *     }
 * }
 */

class Solution {
public:
    bool canAttendMeetings(vector<Interval>& intervals) {
        int n = intervals.size();
        if(n == 0){
            return true;
        }
        vector<vector<int>>tmp;
        for(auto i: intervals){
            tmp.push_back({i.start,i.end});
        }
        sort(tmp.begin(),tmp.end());
        vector<int>lastInterval = tmp[0];
        for(int i=1; i<n; i++){
            if(lastInterval[1] > tmp[i][0]){
                return false;
            }
            else{
                lastInterval = tmp[i];
            }
        }
        return true;
    }
};
