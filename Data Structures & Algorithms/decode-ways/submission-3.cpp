class Solution {
public:
    int recurse(string s,int curr,int n){
        if(curr >= n){
            return 1;
        }

        int ans = 0;
        
        string s1 = s.substr(curr,1);
        string s2 = s.substr(curr,2);

        int singleDigit = stoi(s1);
        int doubleDigit = stoi(s2);

        if(singleDigit >=1 && singleDigit <= 9){
            ans += recurse(s,curr+1,n);
        }

        if(doubleDigit >= 10 && doubleDigit <= 26){
            ans += recurse(s,curr+2,n);
        }

        return ans;
    }

    int numDecodings(string s) {
        int n = s.size();
        return recurse(s,0,n);
    }
};
