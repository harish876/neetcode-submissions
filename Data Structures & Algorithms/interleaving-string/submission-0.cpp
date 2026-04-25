class Solution {
public:
    vector<vector<int>>cache;
    bool dfs(string s1,string s2,string s3,int i,int j,int k){
        //i+j logic here
        if(k == s3.size()){
            return (i == s1.length() && j == s2.length());
        }

        if(cache[i][j] != -1){
            return cache[i][j];
        }

        bool ans = false;
        if(s1[i] == s3[k]){
            ans |= dfs(s1,s2,s3,i+1,j,k+1);
        }
        
        if(s2[j] == s3[k]){
            ans |= dfs(s1,s2,s3,i,j+1,k+1);
        }

        return cache[i][j] = ans;
    }
    bool isInterleave(string s1, string s2, string s3) {
        /*
            ayz
               |
            0
            abc
              |
            0
            abayzc
                 |
        */
        cache.clear();
        cache.resize(s1.size()+1,vector<int>(s2.size()+1,-1));
        return dfs(s1,s2,s3,0,0,0);
    }
};
