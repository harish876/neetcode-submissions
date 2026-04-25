class Solution {
public:
    unordered_map<int,bool>cache;
    bool dfs(string s,vector<string>& wordDict,int curr,int n){
        if(curr >= n){
            return true;
        }

        if(cache.find(curr) != cache.end()){
            return cache[curr];
        }

        bool ans = false;
        for(auto word: wordDict){
            int wordSize = word.size();
            string currWord = s.substr(curr,wordSize);

            if(currWord == word){
                ans |= dfs(s,wordDict,curr+wordSize,n);
            }
        }
        return cache[curr] = ans;
    }

    bool wordBreak(string s, vector<string>& wordDict) {
        int n = s.size();
        return dfs(s,wordDict,0,n);
    }
};
