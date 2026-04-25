class Solution {
public:

    string encode(vector<string>& strs) {
        string result ="";
        for(string s:strs){
            result += to_string(s.size()) + "#" +s;
        }
        cout<<result<<endl;
        return result;
    }

    vector<string> decode(string s) {
        //4#neet4#code4#love3#you
        int n = s.size();
        vector<string>result;
        int i = 0;
        while(i<s.size()){
            int j = i;
            while(s[j] != '#'){
                j++;
            }
            int ssize = stoi(s.substr(i,j-i));
            result.push_back(s.substr(j+1,ssize));
            i = j+1+ssize;
        }
        
        return result;    
    }
};
