class Solution {
public:
    int characterReplacement(string s, int k) {
        /*
            A   A   C   B   A   B   B
            |
                                |   

            len = 6
            
            A - 3
            B - 2
            C - 1
        */
        unordered_map<char,int>mp;
        int start = 0, curr = 0, n = s.size(), maxFreq = 0, result = 0;
        while(curr < n){
            mp[s[curr]]++;

            int max_freq = 0;
            for(auto i:mp){
                max_freq = max(max_freq,i.second);
            }

            
            while((curr-start+1) - max_freq > k){
                mp[s[start]]--;
                start++;
            }

            result = max(result,curr-start+1);
            curr++;
        }

        return result;

    }
};
