class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        set<string>st;
        for(string word: strs){
            string s = word;
            sort(s.begin(),s.end());
            st.insert(s);
        }
        
        int idx = 0;
        vector<vector<string>>result(st.size());
        for(auto i: st){
            for(string word: strs){
                string s = word;
                sort(s.begin(),s.end());
                if(s == i){
                    result[idx].push_back(word);
                }
            }
            idx++;
        }

        return result;
    }
};
