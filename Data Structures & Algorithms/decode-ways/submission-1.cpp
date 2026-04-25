class Solution {
public:
    vector<int>cache;
    int recurse(string s,int curr,int n){
        if(curr >= n){
            return 1;
        }

        if(cache[curr] != -1){
            return cache[curr];
        }

        int singleDigit = s[curr] - '0';
        int doubleDigit = std::stoi(s.substr(curr,2));

        int result = 0;

        if(singleDigit >=1 && singleDigit <= 9){
            result += recurse(s,curr+1,n);
        }

        if(doubleDigit >= 10 && doubleDigit <= 26){
            result += recurse(s,curr+2,n);
        }

        return cache[curr] = result;
    }

    int numDecodings(string s) {
        int n = s.size();
        cache.resize(n+1,-1);
        return recurse(s,0,n);
    }
};
