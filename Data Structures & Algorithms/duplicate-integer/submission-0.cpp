class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        //basic approach is map and check for enumerations
        //other approach is the set
        unordered_set<int>st;

        for(int num: nums){
            if(st.find(num) != st.end()){
                return true;
            }
            else{
                st.insert(num);
            }
        }
        return false;
    }
};