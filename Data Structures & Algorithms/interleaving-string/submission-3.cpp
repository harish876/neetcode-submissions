class Solution {
public:
    vector<vector<int>>cache;
    bool helper(string s1,string s2,string s3,int i,int j){
        if(i + j >= s3.size()){
            return (i >= s1.size() && j>= s2.size());
        }

        if(cache[i][j] != -1){
            return cache[i][j];
        }
        
        bool ans = false;
        if(s1[i] == s3[i+j]){
            ans |= helper(s1,s2,s3,i+1,j);
        }
        if(s2[j] == s3[i+j]){
            ans |= helper(s1,s2,s3,i,j+1);
        }
        return cache[i][j] = ans;
    }

    bool isInterleave(string s1, string s2, string s3) {
        int n = s1.size();
        int m = s2.size();
        cache.resize(n+1,vector<int>(m+1,-1));
        return helper(s1,s2,s3,0,0);
    }
};
