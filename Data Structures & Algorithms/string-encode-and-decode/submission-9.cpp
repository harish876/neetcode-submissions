class Solution {
public:

    string encode(vector<string>& strs) {
        string result = "";
        for(string str: strs){
            result += to_string(str.size()) + "#" + str;
        }
        cout<<result<<endl;
        return result;
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
