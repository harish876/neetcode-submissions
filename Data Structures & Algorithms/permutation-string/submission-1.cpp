class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        /*
            a   b   c
            l   e   c   a   b   e   e
        */

        int start = 0, curr = 0, n = s2.size(), k = s1.size(), result = 0;
        unordered_map<char,int>mp1;
        unordered_map<char,int>mp2;

        for(auto i: s1) mp1[i]++;

        while(curr < n){
            mp2[s2[curr]]++;
            if(curr - start + 1 == k){
                int ctr = 0;
                for(auto i: mp1){
                    if(mp2.find(i.first) != mp2.end() && mp2[i.first] == mp1[i.first]){
                        ctr++;
                    }
                }
                if(ctr == mp1.size()) return true;
                mp2[s2[start]]--;
                if(mp2[s2[start]] == 0) mp2.erase(s2[start]);
                start++;
            }
            curr++;
        }

        return false;;


    }
};
