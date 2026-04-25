class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        /*
            z   x   y   z   x   y   z
            |
                        |
        */

        unordered_map<char,int>mp;
        int start = 0, curr = 0, n = s.size(),result = 0;

        while(curr < n){
            mp[s[curr]]++;
            if(mp[s[curr]] > 1){
                while(mp[s[curr]] > 1){
                    mp[s[start]]--;
                    start++;
                }
            }
            result = max(result,curr-start+1);
            curr++;
        }

        return result;
    }
};
