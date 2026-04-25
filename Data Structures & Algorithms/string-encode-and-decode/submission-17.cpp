class Solution {
public:

    string encode(vector<string>& strs) {
        string encodedString = "";
        int n = strs.size();

        for(int i=0; i<n; i++){
            int k = strs[i].size();
            string delimiter =  "#" + std::to_string(k);
            encodedString += to_string(strs[i].size()) + "#" + strs[i];
        }
        std::cout << "ENCODED STRING: " << encodedString << std::endl;
        return encodedString;
    }

    vector<string> decode(string s) {
        int n = s.size();
        int curr = 0;
        vector<string>result;
        while(curr < n){
            string len = "";
            while(s[curr] != '#'){
                len += s[curr];
                curr++;
            }
            int strlen = stoi(len);
            string tmp = s.substr(curr+1,strlen);
            result.push_back(tmp);
            curr+=(strlen+1);
        }
        return result;
    }  
};
