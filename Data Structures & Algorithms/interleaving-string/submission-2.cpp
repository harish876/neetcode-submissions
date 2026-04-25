class Solution {
public:
    bool helper(string s1,string s2,string s3,int i,int j){
        if(i + j >= s3.size()){
            return (i >= s1.size() && j>= s2.size());
        }
        
        bool ans = false;
        if(s1[i] == s3[i+j]){
            ans |= helper(s1,s2,s3,i+1,j);
        }
        if(s2[j] == s3[i+j]){
            ans |= helper(s1,s2,s3,i,j+1);
        }
        return ans;
    }

    bool isInterleave(string s1, string s2, string s3) {
        return helper(s1,s2,s3,0,0);
    }
};
