class Solution {
public:
    vector<vector<int>>cache;
    int recurse(string t1,string t2, int i,int j){
        if(i >= t1.size() || j >= t2.size()){
            return 0;
        }

        if(cache[i][j] != -1){
            return cache[i][j];
        }

        if(t1[i] == t2[j]){
            return cache[i][j] = 1 + recurse(t1,t2,i+1,j+1);
        }

        return cache[i][j] = max(recurse(t1,t2,i+1,j),recurse(t1,t2,i,j+1));
    }

    int longestCommonSubsequence(string text1, string text2) {
        /*
            - recursion
            - dynamic programming
        */
        int n1 = text1.size();
        int n2 = text2.size();
        cache.clear();
        cache.resize(n1+1,vector<int>(n2+1,-1));
        return recurse(text1,text2,0,0);
    }
};
