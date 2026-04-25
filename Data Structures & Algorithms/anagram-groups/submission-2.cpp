class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        //dumb approach would be the groups are the sorted values 
        // O(n log n)
        vector<vector<string>>result;
        unordered_map<string,vector<string>>mp;
        for(string s: strs){
            string tmp = s;
            sort(tmp.begin(),tmp.end());
            mp[tmp].push_back(s);
        }
        for(auto i:mp){
            result.push_back(i.second);
        }
        return result;
    }
};
