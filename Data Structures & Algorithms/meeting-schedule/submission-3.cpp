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
        sort(intervals.begin(),intervals.end(),[](const Interval i1,const Interval i2){
            return i1.start < i2.start;
        });
        int prevLeaveTime = intervals[0].end;
        for(int i=1; i<n; i++){
            if(prevLeaveTime > intervals[i].start){
                return false;
            }
            else{
                prevLeaveTime = max(prevLeaveTime,intervals[i].end);
            }
        }
        return true;
    }
};
