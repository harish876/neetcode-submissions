class Solution {
public:
    string longestPalindrome(string s) {
        /*
            a b b c
            |     |
        */
        int n = s.size();
        int maxLen = 0;
        string result;
        for(int i=0; i<n; i++){
            //odd length pals
            int start = i;
            int end = i;
            while(start >=0 && end < n && s[start] == s[end]){
                start--;
                end++;
                if(end - start > maxLen){
                    maxLen = end-start;
                    result = s.substr(start+1,maxLen-1);
                }
            }
            //even length pals
            start = i-1;
            end = i;
            while(start >=0 && end < n && s[start] == s[end]){
                start--;
                end++;
                if(end - start > maxLen){
                    maxLen = end-start;
                    result = s.substr(start+1,maxLen-1);
                }
            }
        }
        return result;
    }   
};
