class Solution {
private:
    vector<vector<string>>result;
public:
    bool isPal(string s){
        string tmp = s;
        reverse(s.begin(),s.end());
        return tmp == s;
    }

    void dfs(string s, int curr,int n,vector<string>path){
        if(curr >= n){
            if(count(result.begin(),result.end(),path) == 0) result.push_back(path);
            return;
        }

        for(int len = 1; len <= n; len++){
            string subString = s.substr(curr,len);
            if(!isPal(subString)){
                continue;
            }
            path.push_back(subString);
            dfs(s,curr + len, n, path);
            path.pop_back();
        }
    }

    vector<vector<string>> partition(string s) {
        //dumbass approach
        int n = s.size();
        result.clear();
        dfs(s,0,n,{});
        return result;
    }
};
