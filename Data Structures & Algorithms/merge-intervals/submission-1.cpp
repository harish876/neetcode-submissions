class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        //this is simple
        int n = intervals.size();
        sort(intervals.begin(),intervals.end());
        vector<vector<int>>result = {intervals[0]};
        for(int i=1; i<n; i++){
            int sz = result.size();
            vector<int>lastInterval = result[sz-1];
            if(lastInterval[1] >= intervals[i][0]){
                if(intervals[i][1] > lastInterval[1]){
                    result[sz-1][1] = intervals[i][1];
                }
            }
            else{
                result.push_back(intervals[i]);
            }
        }
        return result;
    }
};
