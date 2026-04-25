class Solution {
public:
    string minWindow(string s, string t) {
        /*
            O   U   Z   O   D   Y   X   A   Z   V
                |
                                    |
            X   Y   Z

            OUZODYX
            ODYXAZ

            shortest
            count_s=3     count_t=3
            map1        map2
            O-2          X-1
            U-1          Y-1
            Z-1          Z-1
            D-1
            Y-1
            X-1

            s =     A   A
                        |
            t =     A   A

            count_s=2     count_t=2


        */
        string result;
        int n = s.size();
        int minLen = n+1;
        int start = 0, curr = 0;

        unordered_map<int,int>mp1;
        unordered_map<int,int>mp2;

        int count_s = 0, count_t = 0;
        for(char c: t){
            mp2[c]++;
        }

        count_t = mp2.size();

        while(curr < n){
            mp1[s[curr]]++;

            if(mp2.find(s[curr]) != mp2.end()){
                if (mp1[s[curr]] == mp2[s[curr]]) {
                    count_s++;
                }
            }

            while(count_s == count_t){
                if(curr-start+1 < minLen){
                    minLen = curr-start+1;
                    result = s.substr(start,minLen);
                }
                
                mp1[s[start]]--;
                if(mp2.find(s[start]) != mp2.end()){
                    if (mp1[s[start]] < mp2[s[start]]) {
                        count_s--;
                    }
                }
                start++;
            }
            curr++;
        } 
        return result;
    }
};
