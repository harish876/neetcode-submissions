class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        /*
            1 2 3 2 2
            0 1 2 3 4
        */
        unordered_map<int,int>mp;
        for(auto i:nums){
            mp[i]++;
        }
        for(auto i:mp){
            if(i.second > 1){
                return i.first;
            }
        }
        return -1;
    }
};
