class Solution {
public:
    vector<int>cache;
    bool helper(string s,vector<string>& wordDict,int curr,int n){
        if(curr >= n){
            return true;
        }

        if(cache[curr] != -1){
            return cache[curr];
        }

        bool ans = false;
        for(string word: wordDict){
            int wordLen = word.size();
            string currWord = s.substr(curr,wordLen);
            if(currWord == word){
                ans |= helper(s,wordDict,curr + wordLen,n);
            }
        }
        return cache[curr] = ans;
    }

    bool wordBreak(string s, vector<string>& wordDict) {
        /*
            "apple| pen | apple"
        */
        int n = s.size();
        cache.resize(n+1,-1);
        return helper(s,wordDict,0,n);
    }
};
