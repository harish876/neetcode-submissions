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
        for(int num: nums){
            mp[num] = 1;
        }

        for(int num: nums){
            int tmp = num; 
            while(mp.find(tmp-1) != mp.end()){
                mp[tmp-1] = max(mp[tmp-1], 1 + mp[tmp]);
                tmp--;
            }
        }
        int result = 0;
        for(auto i:mp){
            //cout << i.first << " " << i.second << endl;
            result = max(result,i.second);
        }

        return result;
    }
};
