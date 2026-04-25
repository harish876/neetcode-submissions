class Solution {
public:
    bool isAnagram(string s, string t) {
        //easiest way is sort both and compare -> O(nlogn)
        // O(n+m)

        map<char,int>mp;

        for(char c: s){
            mp[c]++;
        }

        for(char c: t){
            if(mp.find(c) == mp.end()){
                return false;
            }
            mp[c]--;
        }

        for(auto i: mp){
            if(i.second > 0){
                return false;
            }
        }
        return true;
    }
};
