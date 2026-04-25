class Solution {
public:
    int countSubstrings(string s) {
        int n = s.size();
        int result = 0;
        for(int i=0; i<n; i++){
            int left = i;
            int right = i;

            while(left >= 0 && right < n && s[left] == s[right]){
                result++;
                left--;
                right++;
            } 

            left = i-1;
            right = i;
            while(left >= 0 && right < n && s[left] == s[right]){
                result++;
                left--;
                right++;
            } 
        }
        return result;
    }
};
