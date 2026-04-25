class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        /*
            z   x   y   z   x   y   z
            |
                        |
        */
        int n = s.size();
        int start = 0, curr = 0;
        int result = 0;
        unordered_map<int,int>mp;
        while(curr < n){   
            char currChar = s[curr];
            mp[currChar]++;
            while(mp[currChar] > 1){
                mp[s[start]]--;
                start++;
            }
            result = max(result, curr-start+1);
            curr++;

        }
        return result;
    }
};
