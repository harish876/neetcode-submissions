class Solution {
public:
    bool isPalindrome(string s) {
        string rev = "";
        for(int i=s.size()-1; i>=0; i--){
            char c = s[i];
            if(isdigit(c) && !isalpha(c)){
                rev += c;
            }
            else if(isalpha(c)){
                rev += tolower(c);
            }
            else{
                continue;
            }
        }
        std::cout << rev << std::endl;
        string tmp = rev;
        reverse(tmp.begin(),tmp.end());
        return rev == tmp;
    }
};
