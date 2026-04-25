class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        /*
            2,20,4,10,3,4,5


            0,3,2,5,4,6,1,1
              |

            0,3,2,5,6,1
            
            0 - 4
            3 - 1
            2 - 2
            5 - 1
            4 - 1
            6 - 1
            1 - 3
        */

        unordered_map<int,int>mp;
        for(auto i:nums) mp[i] = 1;
        int result = 0;
        for(int num: nums){
            if(mp.find(num-1) == mp.end()){
                int len = 0;
                while(mp.find(num + len) != mp.end()){
                    len++;
                }
                result = max(result,len);
            }
        }
        return result;
    }
};
