class Solution {
public:
    int recurse(string s,string t,int i,int j){
        if(j == t.size()){  
            return 1;
        }

        if(i == s.size()){  
            return 0;
        }
        
        int ans = 0;
        if(s[i] == t[j]){
            ans += recurse(s,t,i+1,j+1);
        }

        ans += recurse(s,t,i+1,j);

        return ans;

    }
    int numDistinct(string s, string t) {
        /*
            c   a   a   a   t
                        |
            c   a   t
                    |
        */
        return recurse(s,t,0,0);
    }
};
