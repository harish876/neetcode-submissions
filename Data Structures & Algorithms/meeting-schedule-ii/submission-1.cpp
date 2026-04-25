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
        //divide into non overlapping intervals
        if(intervals.size() == 0){
            return 0;
        }

        sort(intervals.begin(),intervals.end(),[](const Interval& i1,const Interval& i2){
            if(i1.start == i2.start){
                return i1.end < i2.end;
            }
            return i1.start < i2.start;
        });

        vector<vector<Interval>>buckets;
        buckets.push_back({intervals[0]});
        for(auto it = intervals.begin()+1; it != intervals.end(); it++){
            Interval i = *it;
            bool added = false;
            for(auto &bucket: buckets){
                Interval lastInterval = *(bucket.rbegin());
                if(lastInterval.end <= i.start){
                    bucket.push_back(i);
                    added = true;
                    break;
                }
            }
            if(!added){
                buckets.push_back({i});
            }
        }

        int bucket_num = 1;
        for(auto bucket: buckets){
            cout<<"Bucket Number"<<bucket_num<<":"<<endl;
            for(auto intervals: bucket){
                cout<<intervals.start<<" - "<<intervals.end<<endl;
            }
            bucket_num++;
        }
        return buckets.size();
    }
};
