class Solution {
public:
    vector<vector<int>>cache;
    int recurse(string s,string t,int i,int j){
        if(j == t.size()){  
            return 1;
        }

        if(i == s.size()){  
            return 0;
        }

        if(cache[i][j] != -1){
            return cache[i][j];
        }
        
        int ans = 0;
        if(s[i] == t[j]){
            ans += recurse(s,t,i+1,j+1);
        }

        ans += recurse(s,t,i+1,j);

        return cache[i][j] = ans;

    }
    int numDistinct(string s, string t) {
        /*
            c   a   a   a   t
                        |
            c   a   t
                    |
        */
        int m = s.size();
        int n = t.size();
        cache.resize(m,vector<int>(n,-1));
        return recurse(s,t,0,0);
    }
};
