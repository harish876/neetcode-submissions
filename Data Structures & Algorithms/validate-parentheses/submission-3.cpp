class Solution {
public:
    bool isValid(string s) {
        stack<char>st;
        for(char c:s){
        if(
            !st.empty() && ((c == ']' && st.top() == '[') 
            || (c == ')' && st.top() == '(')
            || (c == '}' && st.top() == '{')
            )){
                st.pop();
            }
        else{
            st.push(c);
        }
        }
        return st.size() == 0;
    }
};
