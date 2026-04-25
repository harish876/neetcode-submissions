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
    int minMeetingRooms(vector<Interval>& intervals) {
        //bucketing
        //min number of buckets
        /*
            (1,10),(2,3),(4,5),(6,7),(8,9)

            buckets = [40,10,]
        */
        int n = intervals.size();
        if(n == 0){
            return 0;
        }

        vector<int>buckets;

        sort(intervals.begin(),intervals.end(),[](const Interval& i1,const Interval& i2){
            if(i1.start == i2.start){
                return i1.end < i2.end;
            }
            return i1.start < i2.start;
        });

        buckets.push_back(intervals[0].end);
        for(int i=1; i<n; i++){
            int curr_arrival = intervals[i].start;
            int curr_leaving = intervals[i].end;
            bool added = false;

            for(int j=0; j<buckets.size(); j++){
                if(curr_arrival >= buckets[j]){
                    added = true;
                    buckets[j] = max(buckets[j],curr_leaving);
                    break;
                }
            }

            if(!added){
                buckets.push_back(curr_leaving);
            }
        }

        return buckets.size();
    }
};
