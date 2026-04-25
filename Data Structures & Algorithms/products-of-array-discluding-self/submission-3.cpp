class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int>pre1(n,1);
        for(int i=1; i<n; i++){
            pre1[i] = nums[i-1] * pre1[i-1]; 
        }
        int pre2 = 1;
        for(int i=n-1; i>=0; i--){
            pre1[i] = pre1[i] * pre2;
            pre2 *= nums[i];
        }
        return pre1;

    }
};
