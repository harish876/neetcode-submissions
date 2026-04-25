class Solution {
public:
    int countSubstrings(string s) {
        //O(n^2)
        /*
            a b c
            |
        */
        int n = s.size();
        int result = 0;
        for(int i=0; i<n; i++){
            //odd length
            int start = i;
            int end = i;
            while(start >=0 && end < n && s[start] == s[end]){
                start--;
                end++;
                result++;
            }

            //even length
            start = i-1;
            end = i;
            while(start >=0 && end < n && s[start] == s[end]){
                start--;
                end++;
                result++;
            }
        }
        return result;
    }
};
